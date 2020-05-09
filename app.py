import os
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_pymongo import PyMongo, pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId 
from os import path

if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'college_cookbook'
app.config["MONGO_URI"] = os.environ["MONGO_URI"]
app.config['SECRET_KEY'] = os.urandom(24)
mongo = PyMongo(app)

# Collections

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = request.form.to_dict()
	user_in_db = users_collection.find_one({'username': form['username']})
	# Check for user in database
	if user_in_db:
		# If passwords match (hashed / real password)
		if check_password_hash(user_in_db['password'], form['password']):
			# Log user in (add to session)
			session['user'] = form['username']
			# If the user is admin redirect him to admin area
			if session['user'] == "user":
				return redirect(url_for('get_recipes'))
			else:
				flash("Logged in successful!")
				return redirect(url_for('get_recipes', user=user_in_db['username']))
			
		else:
			flash("Wrong password or username!")
			flash("Try login again")
			return redirect(url_for('get_recipes'))
	else:
		flash("You need to signup !")
		return redirect(url_for('get_recipes'))

	

# Sign up
@app.route('/register', methods=['GET', 'POST'])
def register():
	# Check if user is not logged in already
	if 'user' in session:
		flash('Already sign in!')
		return redirect(url_for('get_recipes'))
	if request.method == 'POST':
		form = request.form.to_dict()
		# Check if the password and password1 actually match 
		if form['password'] == form['password1']:
			# If so try to find the user in db
			user = users_collection.find_one({"username" : form['username']})
			print(form)
			if user:
				flash(f"{form['username']} already exists!")
				return redirect(url_for('get_recipes'))
			# If user does not exist register new user
			else:				
				# Hash password
				hash_pass = generate_password_hash(form['password'])
				#Create new user with hashed password
				users_collection.insert_one(
					{
						'username': form['username'],
						'password': hash_pass
					}
				)
				# Check if user is actually saved
				user_in_db = users_collection.find_one({"username": form['username']})
				if user_in_db:
					# Log user in (add to session)
					session['user'] = user_in_db['username']
					return redirect(url_for('get_recipes', user=user_in_db['username']))
				else:
					flash("There was a problem saving your profile")
					return redirect(url_for('get_recipes'))

		else:
			flash("Passwords don't match!")
			return redirect(url_for('get_recipes'))
		
	return render_template("recipes")

# Log out
@app.route('/logout')
def logout():
	# Clear the session
	session.clear()
	flash('You were logged out!')
	return redirect(url_for('get_recipes'))


@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    if 'user' in session:
      return render_template("recipes.html", recipes=mongo.db.recipes.find(), user = session['user'])
    else:
      return render_template("recipes.html", recipes=mongo.db.recipes.find())

 
    
@app.route('/stats')
def stats():
    return render_template("stats.html", 
    recipes=mongo.db.recipes.find())


@app.route('/add_recipe')
def add_recipe():
    if 'user' in session:
        categories=mongo.db.categories.find()
        flash('Recipe added successfully')
        return render_template('add_recipe.html', categories = categories)
    else:
        return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route ('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes=mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>', methods=['POST'])
def edit_recipe(recipe_id):
    if 'user' in session:
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        all_categories = mongo.db.categories.find()
        flash('Recipe edited')
        return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)
    else: 
        return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes=mongo.db.recipes
    recipes.update_one({'_id': ObjectId(recipe_id)}, 
    { "$set":
       {
        "category_name":request.form.get('category_name'),
        "recipe_name":request.form.get('recipe_name'),
        "recipe_image":request.form.get('recipe_image'),
        "Serves":request.form.get('Serves'),
        "Prep_Time":request.form.get('Prep_Time'),
        "Cook_Time":request.form.get('Cook_Time'),
        "recipe_description":request.form.get('recipe_description'),
        "Author":request.form.get('Author'),
        "Ingredients":request.form.get('Ingredients'),
        "Instructions":request.form.get('Instructions')
        }
     }
    )
    return redirect(url_for('get_recipes'))
    

      
@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 'user' in session:
        mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
        flash('Recipe deleted')
    return redirect(url_for('get_recipes'))
    
@app.route('/how_to/<recipe_id>')
def how_to(recipe_id):
   
        the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        all_categories = mongo.db.categories.find()
        return render_template('how_to.html', recipe=the_recipe, categories=all_categories)
  

"""
Error handling
"""

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def wrong_req(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)