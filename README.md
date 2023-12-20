# RecipeOrganizer
This project is built using Python and Tkinter for GUI.
# Project Title :  Recipe Organizer
## Brief_Explanation: 
It is an application which having the functionalities to Add, Delete, View, Edit, Sort and Search the Recipe. It is built using Tkinter GUI python library. 
# Technology Used:
Python Programming Language, Tkinter for GUI
# Flow of Creation:
* Firstly import all the important python library and module such as tkinter, PIL, requests, webbrowser, ImageTk, Image, io and BytesIO.
* Creating class LinkLabel which is basically handling the URL hyperlink.
* Creating RecipeInfo class where all the details of Recipe is listed such as Name, ingredients, instruction means how to prepare, Category of Recipe.
* Creating RecipeOrganizer class which basically handling all the fucntionalities such as Adding recipe to the listbox, deleting recipe from the listbox, Editing existing recipe from the listbox, Sorting Recipe in alphabetical and Recipe category manner, Search recipe method where user will search for the particular recipe and can also see the steps of preparing the recipe by navigating from Recipe Link button to the default web Browser of user’s system.
* Updating the lisbox everytime when user edit and sort the recipe from the listbox.
* Edamam Application id and Apikey is used for fetching the recipe info from the JSON api.
* Create Tkinter main window and Pack or close the tkinter main window i.e,. root window after creating the object of RecipeOrganizer class.
# Flow of Execution:
* Firstly you have to run the exe file then a Gui window will be opened.
* Click on Add recipe button if user want to add recipe to the listbox of main window.
* For viewing, editing or deleting the particular recipe user have to select that recipe from the listbox. For sorting click on sort recipe button.
* Click search button to search Recipe of your own choice by their name.
