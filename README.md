# College Cookbook by Stefan Sarbu

See the project live at http://college-cookbook-stef.herokuapp.com/

This is a basic CRUD online cookbook, where visitors can see a list of recipes added
by anyone who wishes to. Recipes can be added, edited and deleted only by 
logged in users.

# UX

The app is a very basic one, but functional and performs well the CRUD operations.

The final project has some differences in layout from the designs done in the planning.
It was noted during development that these changes were necessary to provide a 
better user experience.

#### User stories:
1. As a curious user/visitor, I would like to be able to see through a list of recipes with at least 3-4 categories. The College Cookbook is inspired from the famous book of Pamela Ellgen, author of
this great recipe cookbook which was written and published by her especially for the young and 
restless students, but not only for them. At this moment all recipes on the app belong to the author of the book.

Here you can have details about Pamela's cookbook: https://www.amazon.com/5-Ingredient-College-Cookbook-Healthy-Recipes/dp/1623158575.

2. As a chef, I would like to be able to store any recipes I create, in order to 
access and share with others. 

# Features

## Existing Features
The application can be used with or without a user login, however some features 
are only available to logged in users.

Any user of the website is able to see the recipes from the app. 

Users can create an account, this is very basic in that usernames and passwords 
are stored in the database in a collection 'Users'.

Once an account has been created and user is logged in, will have the option 
to add their own recipe(s), edit and delete.

Adding a recipe will create a new document in the database's 'Recipes' collection.
That recipe will then be available to see along with the other recipes.

From an existing recipe, a user will be able to edit or delete. If they choose to 
delete a recipe, the document in the database for that recipe will be removed together
with a confirmation message.


The app also features custom 404 and 500 error pages.


## Features Left to Implement

#### More/Custom categories
At the moment the app has only 6 categories to choose from for the recipes. The app would look better if would have the option to allow user to add a category.  

#### Rating and Views
Maybe some of the passionated chef would love to check the number of views and the rating for the recipes shared with others.

#### Editing
Keeping track of which users have edited a recipe by adding an array
to the document showing each individual edit such as:
```"edits" : [{"date" : 00/00/0000, "username" : "person", "fields_edited" : ['name', 'ingredients', 'image', 'category']```

#### User contribution
A logged in user should only be able to delete the recipe(s) that was created by that particular user and not someone else's recipe. For now, I believe that any visitor will only look after recipes and trying to cook them and not deleting someone else's effort of sharing.

#### User profiles
As mentioned in User Contribution section if a user has an account on a site such as this, they would expect to be able to go to a personal profile page where they can see their own recipes and edit from there. This is something that should be implemented in a future version.

#### Pagination& Search
I was struggling to implement the pagination to the app in order for the visitor/user to have an easier UX but unfortunately I was not able to deliver this feature in time. .

# Technologies Used
The main logic of this application is written in [Python](https://www.python.org) 
using the [Flask](http://flask.pocoo.org/) framework to handle the routes and 
page rendering, and [PyMongo](https://api.mongodb.com/python/current/) for CRUD operations.

Pages are written in [HTML](https://www.w3.org/html/) using 
[CSS3](https://www.w3.org/Style/CSS/Overview.en.html) for styling and 
[JavaScript](https://www.javascript.com/) for enhanced effects and some of the 
button functions, specifically with [JQuery](https://jquery.com/)to minimalise 
the amount of code required.

The main page layout and styles are from https://getbootstrap.com/docs/4.0/getting-started/introduction/.

The app uses two Python files, app.py for the main Flask app routing and the CRUD 
functions, and env.py for keeping secure the database.

### Database
The site uses [MongoDB](https://www.mongodb.com/) for data storage.

There are three collections in the database.

Users: This is where user data is stored, including username, password and a list 
of recipes that have been rated by that user.

Categories: holds one document for each category, giving the name and type of 
category.

Recipes: The collection of all active recipes. Any deleted recipes are marked with 
the username of the user that deleted it and moved to the Deleted Recipes collection.



# Testing
All HTML and CSS has been run through the W3 validators and cleared of errors.

All pages have been tested on all screen sizes. This has been done via Google Chrome
developer tools and by testing on my own personal phone and ipad.

All of the actions below have been tested on multiple browsers. These include Chrome, 
Safari, Edge, Firefox and Opera.

1. 
- From the main page, all recipes are available.
- Click How To button to get more details about the recipe.
- Click Back button or logo to go back to home page.

2. As a chef, I would like to be able to store any recipes I create, in order to 
   access and share with others.

- From the main page, click Log In.
- If not registered, click Sign up Button .
- Try entering a different password in the 'Re-enter Password' box.
- Enter correct details and click Create User.
- Click Log Out.
- Click Log In. View, add, edit or delete a recipe



##### Testing Error Handlers
- Try going to http://college-cookbook-stef.herokuapp.com/nonexistingpage and 
observe the custom 404 error.
- Click the image to ensure the link is active.
- Click the button to go back to the previous page.

### Issues

###### Images issue
I found that is easier for the user to add the link from a recipe instead of 
uploading images to the website which at a certain time will load the app too much.
The user has to search for google for an appropriate image for its recipe and right click
"Copy image address" and then paste it to recipe image section.
This might be either a good thing or an issue, depending on the person/user. 
Many problems with indentation for python, I find it difficult to try fixing the errors, and debugging. 

##### Caching
There were some caching issues with Cloud9 ide and/or the browser, but 
performing a 'hard' refresh (Ctrl+F5) fixed it.

# Deployment

The application is currently hosted live on Heroku; the code in the live version 
is identical to that here on github.

It can be installed with the following steps:
1. Download the git repository
2. Sign up/login to Heroku.com
3. From the dashboard click Create New App
4. Enter a unique name and your region and click Create
5. From your command line, enter `heroku` to ensure heroku is installed (if not 
installed this can be done with `sudo snap install --classic heroku`)
6. CLI: `heroku login`
7. Enter your credentials for heroku.com
8. CLI: `sudo pip3 install Flask`
9. CLI: `sudo pip3 install pymongo`
10. CLI: `sudo pip3 freeze --local > requirements.txt`
11. CLI: `echo web: python run.py > Procfile`
12. CLI: `git add .`
13. CLI: `git commit -m "initial deployment"`
14. CLI: `git push -u heroku master`
15. CLI: `heroku ps:scale web=1`
16. From heroku.com app settings: set config vars to IP : 0.0.0.0, PORT : 5000 and 
MONGO_DBNAME : college_cookbook, 
ensuring that you update the username and password accordingly.
17. Click More > Restart all Dynos
18. App should now be live at https://your-app-name.herokuapp.com/

# Credits
## Content
At the moment all recipes on this website are credited to the author Pamela Ellgen accordingly. 


## Media
Link for Recipe's images can be found in the recipe image url section on each recipe added by me. 
Link for the video on the main page is from Pamela Ellgen's YouTube channel:
https://www.youtube.com/watch?v=JjHHWbmtqfM


## Acknowledgements
This project was based on a brief written by Code Institute to fulfill requirements 
of their Data Centric Development module (part of the Full Stack Web Developer course).

 I found the [Pretty Printed](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
 YouTube channel a huge help in learning about Flask sessions and error handling.

 Special thanks to the Code Institute's 24/7 tutor team (Tim, Kevin, Samanatha, Michael, Stephen, Haley, Chris and Heather). 
 
 Many thanks also to Rahul Lakhanpal who is my Code Institute mentor for this project, for offering 
 ideas and solutions to various issues throughout the project, as well as endless 
 patience and understanding!

