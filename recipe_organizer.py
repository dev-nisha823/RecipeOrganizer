from tkinter import *
from tkinter import simpledialog, messagebox
from io import BytesIO
from PIL import ImageTk, Image
import requests
import webbrowser

# class LinkLabel is a label acting as a hyperlink.
class LinkLabel(Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(cursor="hand2", text="Recipe Link", bg="white",fg="blue", font=("Times New Roman", 15,"bold"),underline=-1)
    #  Method sets the URL for the hyperlink.
    def set_link(self, url):
        self.url = url
    # Method opens the URL in the default web browser when the label is clicked.
    def open_link(self, event):
        webbrowser.open_new(self.url)


# class RecipeInfo containing all the details of Recipe 
class RecipeInfo:
    # Constructor initializes the recipe details such as name, ingredients, instructions, and category.
    def __init__(self, name, ingredients, instructions, category):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        
# class RecipeOrganizer responsible for managing the recipe organizer GUI and functionality.
class RecipeOrganizer:
    # Constructor initializes the main window (root) and sets its properties.
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x700")
        self.root.title("Recipe GUI")
        self.root.configure(bg="black")

        # List to store recipes
        self.recipes = []
        
        # setting background image for Main window
        # Replace "your_image_url" with the URL of the image you want to use
        image_url = "https://images.unsplash.com/photo-1490645935967-10de6ba17061?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fHJlY2lwZXxlbnwwfHwwfHx8MA%3D%3D"
        self.bg_image = self.download_image(image_url)

        # Set background image for the main window
        background_label = Label(self.root, image=self.bg_image,bg="black")
        background_label.place(relwidth=1, relheight=0.5)
        
        # GUI components
        Upper_Label = Label(self.root, text="Welcome to the Recipe Organizer", bg="grey", font=("Times New Roman", 18))
        Upper_Label.pack(side=TOP, fill=X)

        Left_Label = Label(self.root, bg="grey", width=3)
        Left_Label.pack(side=LEFT, fill=Y)

        Right_Label = Label(self.root, bg="grey", width=3)
        Right_Label.pack(side=RIGHT, fill=Y)

        Bottom_Label = Label(self.root, bg="grey", width=5)
        Bottom_Label.pack(side=BOTTOM, fill=X)

        # Frame for Listbox
        listbox_frame = Frame(self.root, bg="black")
        listbox_frame.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Listbox where the Recipe will be added
        self.recipe_listbox = Listbox(listbox_frame, selectmode=SINGLE)
        self.recipe_listbox.configure(width=40)
        self.recipe_listbox.pack(pady=10)

        # Frame for Buttons
        button_frame = Frame(self.root, bg="black")
        button_frame.place(relx=0.5, rely=0.9, anchor=CENTER)

        # Add button to add New recipe
        add_button = Button(button_frame, text="Add Recipe", command=self.add_recipe, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        add_button.pack(side=LEFT, padx=5)

        # View button to see the information of selected Recipe
        view_button = Button(button_frame, text="View Recipe", command=self.view_recipe, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        view_button.pack(side=LEFT, padx=5)

        # Edit button to edit the previous recipe that added inside the Listbox
        edit_button = Button(button_frame, text="Edit Recipe", command=self.edit_recipe, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        edit_button.pack(side=LEFT, padx=5)

        # Delete button to delete the selected recipe of the Listbox
        delete_button = Button(button_frame, text="Delete Recipe", command=self.delete_recipe, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        delete_button.pack(side=LEFT, padx=5)
        
        # Button for sorting recipes of recipe listbox in alphabetical manner
        sort_button = Button(button_frame, text="Sort Recipes", command=self.sort_recipes, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        sort_button.pack(side=LEFT, padx=5)
        
        # Add the Search button
        search_button = Button(button_frame, text="Search Recipe", command=self.search_recipe, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        search_button.pack(side=LEFT, padx=5)
        

    # Function to add a new recipe to the list
    def add_recipe(self):

        # Create a new Toplevel window for the custom dialog
        Add_Recipe_window = Toplevel()
        Add_Recipe_window.title("Add Recipe")
        Add_Recipe_window.geometry("800x600")
        Add_Recipe_window.configure(bg="#FFC5C5")
        

        # Variables to store the input values
        name_var = StringVar()
        category_var = StringVar()

        # Labels and Entry fields for the recipe details
        Label(Add_Recipe_window, text="Recipe Name:", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=0, column=0, padx=10, pady=10)
        Entry(Add_Recipe_window, textvariable=name_var, font=("Times New Roman", 11), width=50).grid(row=0, column=1, padx=10, pady=10)

        Label(Add_Recipe_window, text="Recipe Ingredients (Numbered Order):", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=1, column=0, padx=10, pady=10)
        ingredients_entry = Text(Add_Recipe_window, height=7, font=("Times New Roman", 11), width=50)
        ingredients_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(Add_Recipe_window, text="Recipe Instructions (Step Manner):", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=2, column=0, padx=10, pady=10)
        instructions_entry = Text(Add_Recipe_window, height=7, font=("Times New Roman", 11), width=50)
        instructions_entry.grid(row=2, column=1, padx=10, pady=10)

        Label(Add_Recipe_window, text="Recipe Category:", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=3, column=0, padx=10, pady=10)
        Entry(Add_Recipe_window, textvariable=category_var, font=("Times New Roman", 11), width=50).grid(row=3, column=1, padx=10, pady=10)

        # Button to save the recipe that user wants to add inside the Listbox
        save_button = Button(
            Add_Recipe_window,
            text="Save Recipe",
            command=lambda: self.save_recipe(
                Add_Recipe_window, name_var, ingredients_entry, instructions_entry, category_var
            ),
            fg="white",
            bg="black",
            font=("Times New Roman", 13)
        )
        save_button.grid(row=4, column=1, pady=10)

    # Function to save the recipe and update the list
    def save_recipe(self, Add_Recipe_window, name_var, ingredients_entry, instructions_entry, category_var):
        name = name_var.get()
        ingredients = ingredients_entry.get("1.0", END).strip()
        instructions = instructions_entry.get("1.0", END).strip()
        category = category_var.get()

        if name:
            recipe = RecipeInfo(name, ingredients, instructions, category)
            self.recipes.append(recipe)
            self.update_listbox()
            messagebox.showinfo("Recipe Added", f"Recipe '{name}' added successfully!")
            Add_Recipe_window.destroy()  # Close the Add_Recipe_window 

    # Function to view the selected recipe
    def view_recipe(self):
        selected_recipe_index = self.recipe_listbox.curselection()
        if selected_recipe_index:
            selected_recipe = self.recipes[selected_recipe_index[0]]
            messagebox.showinfo("Recipe", f"Recipe Name: {selected_recipe.name}\n\n"
                                          f"Ingredients: \n{selected_recipe.ingredients}\n\n"
                                          f"Instructions: \n{selected_recipe.instructions}\n\n"
                                          f"Category: {selected_recipe.category}")
    
    # # Function to edit the selected recipe
    def edit_recipe(self):
        selected_recipe_index = self.recipe_listbox.curselection()
        if selected_recipe_index:
            selected_recipe = self.recipes[selected_recipe_index[0]]

            # Create a new Toplevel window for the custom dialog for editing the recipe
            edit_recipe_window = Toplevel()
            edit_recipe_window.title("Edit Recipe")
            edit_recipe_window.geometry("800x600")
            edit_recipe_window.configure(bg="#FFC5C5")

            # Variables to store the input values
            name_var = StringVar(value=selected_recipe.name)
            category_var = StringVar(value=selected_recipe.category)

            # Labels and Entry fields for the recipe details which user will edit
            Label(edit_recipe_window, text="Recipe Name:", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=0, column=0, padx=10, pady=10)
            Entry(edit_recipe_window, textvariable=name_var, font=("Times New Roman", 11), width=50).grid(row=0, column=1, padx=10, pady=10)

            Label(edit_recipe_window, text="Recipe Ingredients (Numbered Order):", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=1, column=0, padx=10, pady=10)
            ingredients_entry = Text(edit_recipe_window, height=7, font=("Times New Roman", 11), width=50)
            ingredients_entry.insert(END, selected_recipe.ingredients)  # Pre-fill with existing ingredients
            ingredients_entry.grid(row=1, column=1, padx=10, pady=10)

            Label(edit_recipe_window, text="Recipe Instructions (Step Manner):", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=2, column=0, padx=10, pady=10)
            instructions_entry = Text(edit_recipe_window, height=7, font=("Times New Roman", 11), width=50)
            instructions_entry.insert(END, selected_recipe.instructions)  # Pre-fill with existing instructions
            instructions_entry.grid(row=2, column=1, padx=10, pady=10)

            Label(edit_recipe_window, text="Recipe Category:", font=("Times New Roman", 13,"bold"), bg="#96EFFF",width=30).grid(row=3, column=0, padx=10, pady=10)
            Entry(edit_recipe_window, textvariable=category_var, font=("Times New Roman", 11), width=50).grid(row=3, column=1, padx=10, pady=10)

            # Button to save the edited recipe
            save_button = Button(
                edit_recipe_window,
                text="Save Changes",
                command=lambda: self.save_changes(
                    selected_recipe, edit_recipe_window, name_var, ingredients_entry, instructions_entry, category_var
                ),
                fg="white",
                bg="black",
                font=("Times New Roman", 13)
            )
            save_button.grid(row=4, column=1, pady=10)

    def save_changes(self, recipe, edit_recipe_window, name_var, ingredients_entry, instructions_entry, category_var):
        recipe.name = name_var.get()
        recipe.ingredients = ingredients_entry.get("1.0", END).strip()  # Get all content from line 1 to the end
        recipe.instructions = instructions_entry.get("1.0", END).strip()  # Get all content from line 1 to the end
        recipe.category = category_var.get()

        self.update_listbox()
        messagebox.showinfo("Recipe Updated", f"Recipe '{recipe.name}' updated successfully!")
        edit_recipe_window.destroy()  # Close the edit_recipe_window window
    
    # Function to delete the selected recipe by user confirmation
    def delete_recipe(self):
        selected_recipe_index = self.recipe_listbox.curselection()
        # if else condition to ask from the user that whether user want to delete the selected Recipe or not by clicking Yes or No
        if selected_recipe_index:
            result = messagebox.askyesno("Delete Recipe", "Are you sure you want to delete the selected recipe from the recipe_listbox?")
            if result:
                self.recipes.pop(selected_recipe_index[0])
                self.update_listbox()
                
    # Function to sort recipes in alphabetical manner
    def sort_recipes(self):
        self.recipes.sort(key=lambda x: x.name.lower())
        self.update_listbox()
        
        # Create a new window for displaying sorted recipes by category
        sort_window = Toplevel()
        sort_window.title("Sorted Recipes by Category")
        sort_window.geometry("400x800")
        sort_window.configure(bg="#BB9CC0")
        
        
        # Create a dictionary to store frames for each category
        category_frames = {}

        # Populate frames with recipes
        for recipe in self.recipes:
            category = recipe.category

            if category not in category_frames:
            # Create a new frame for the category
                category_frame = Frame(sort_window, padx=10, pady=10)
                category_frame.configure(bg="#BB9CC0")
                category_frame.pack(side=TOP, fill=BOTH, expand=True)
            
                # Label for the category
                category_label = Label(category_frame, text=f"{category} Recipes", font=("Times New Roman", 14, "bold"))
                category_label.configure(bg="#BB9CC0")
                category_label.pack(side=TOP)
            
                # Listbox for displaying recipes in the category
                category_listbox = Listbox(category_frame, selectmode=SINGLE, font=("Times New Roman", 14))
                category_listbox.pack(side=TOP, fill=BOTH, expand=True)
            
                # Save the frame in the dictionary
                category_frames[category] = category_frame
            else:
                # Use existing frame for the category
                category_frame = category_frames[category]
                category_listbox = category_frame.winfo_children()[1]  # Assuming label is the first and listbox is the second

            # Insert the recipe into the corresponding listbox
            category_listbox.insert(END, recipe.name)
        
        # Button to close the sort window
        close_button = Button(sort_window, text="Close", command=sort_window.destroy, bg="lightblue", font=("Times New Roman", 13, "bold"), fg="black")
        close_button.pack(side=BOTTOM, pady=10)
        
    # Function to search recipes
    def search_recipe(self):
        # Create a new Toplevel window for the search dialog
        search_window = Toplevel()
        search_window.title("Search Recipe")
        search_window.geometry("610x100")
        search_window.configure(bg="#FFF5C2")

        # Label and Entry for the search query
        Label(search_window, text="Enter Recipe Name:", font=("Times New Roman", 14,"bold"),bg="#7071E8").grid(row=0, column=0, padx=10, pady=10)
        search_entry = Entry(search_window, font=("Times New Roman", 14), width=30)
        search_entry.grid(row=0, column=1, padx=10, pady=10)

        # Button to perform the search
        search_button = Button(search_window, text="Search", command=lambda: self.perform_search(search_entry.get()), font=("Times New Roman", 15,"bold"), fg="white", bg="black")
        search_button.grid(row=0, column=2, pady=10, padx=10)

    # function to perform search operation
    def perform_search(self, query):
        # Edamam application ID and apikey
        edamam_app_id = 'Your Edamam Application ID'
        api_key = 'Your Edamam API KEY'  
        url = f"https://api.edamam.com/search?q={query}&app_id={edamam_app_id}&app_key={api_key}"
        
        try:
            response = requests.get(url)
            data = response.json()

            if 'hits' in data:
                # Display the first recipe found in a new window
                if data['hits']:
                    recipe = data['hits'][0]['recipe']
                    self.display_recipe_details_edamam(recipe)
                else:
                    messagebox.showinfo("Search Result", "No matching recipes found.")
            else:
                messagebox.showerror("Error", "Failed to fetch data from the Edamam API.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    # Function to display the recipe details from Edamam API
    def display_recipe_details_edamam(self, recipe):
        edamam_app_id = 'Your Edamam Application ID'
        api_key = 'Your Edamam API KEY'
        url = f"https://api.edamam.com/search?q={recipe.get('label', '')}&app_id={edamam_app_id}&app_key={api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if 'hits' in data and data['hits']:
                recipe_details = data['hits'][0]['recipe']
                
                # Display recipe details in a new window
                recipe_details_window = Toplevel()
                recipe_details_window.title(recipe_details['label'])
                recipe_details_window.geometry("500x700")
                recipe_details_window.configure(bg="#3081D0")
                

                # Example: Display recipe image
                if 'image' in recipe_details:
                    image_url = recipe_details['image']
                    response = requests.get(image_url)
                    img_data = response.content
                    image = Image.open(BytesIO(img_data))
                    image = ImageTk.PhotoImage(image)
                    image_label = Label(recipe_details_window, image=image)
                    image_label.image = image
                    # Set border properties of recipe image
                    image_label.config(highlightthickness=2,highlightbackground="black")
                    image_label.pack()

                # Create a frame for the details
                details_frame = Frame(recipe_details_window, bg="grey")
                details_frame.pack(pady=10)
                
                # Example: Display other details (modify as needed)
                Label(details_frame, text=f"Title: {recipe_details['label']}", bg="grey",font=("Times New Roman", 12,"bold"), justify=LEFT).pack()


                # Display ingredients with bullet points and left alignment
            if 'ingredients' in recipe_details:
                ingredients_label = Label(details_frame, text="Ingredients:", bg="grey", font=("Times New Roman", 12, "bold"), justify=LEFT)
                ingredients_label.pack()

                # Use a Text widget to display ingredients
                ingredients_text = Text(details_frame, wrap=WORD, font=("Times New Roman", 12), height=10, width=40)
                ingredients_text.pack()

                for index, ingredient in enumerate(recipe_details['ingredients'], start=1):
                    # Insert each ingredient with a bullet point
                    ingredients_text.insert(END, f"• {ingredient['text']}\n")

                # Display instructions
                if 'url' in recipe_details:
                    url_label = LinkLabel(recipe_details_window, text="Source URL", fg="black", cursor="hand2")
                    url_label.pack()
                    url_label.bind("<Button-1>", lambda event: webbrowser.open_new(recipe_details['url']))

            else:
                messagebox.showerror("Error", "Failed to fetch recipe details from the API.")

        except requests.exceptions.HTTPError as http_err:
            messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
    # Function to update the listbox with the current recipe list
    def update_listbox(self):
        self.recipe_listbox.delete(0, END)
        for recipe in self.recipes:
            self.recipe_listbox.insert(END, f"{recipe.name} - {recipe.category}")
            
    # Function to set the background image for the main window of Recipe organizer
    def download_image(self, url):
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        
        # Get the content (image data) from the response
        img_data = response.content
        
        # Open the image using the PIL (Pillow) library
        image = Image.open(BytesIO(img_data))
        
        # Convert the PIL image to a Tkinter-compatible format (PhotoImage)
        return ImageTk.PhotoImage(image)

# Create the main window
root = Tk()
# object of class RecipeOrganizer
recipe = RecipeOrganizer(root)
root.mainloop()
