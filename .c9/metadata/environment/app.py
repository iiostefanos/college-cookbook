{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":55,"column":39},"end":{"row":55,"column":40},"action":"insert","lines":["("],"id":407}],[{"start":{"row":50,"column":48},"end":{"row":50,"column":49},"action":"remove","lines":["]"],"id":408}],[{"start":{"row":50,"column":48},"end":{"row":50,"column":49},"action":"insert","lines":[")"],"id":409}],[{"start":{"row":51,"column":48},"end":{"row":51,"column":49},"action":"remove","lines":["]"],"id":410}],[{"start":{"row":51,"column":48},"end":{"row":51,"column":49},"action":"insert","lines":[")"],"id":411}],[{"start":{"row":52,"column":66},"end":{"row":52,"column":67},"action":"remove","lines":["]"],"id":412},{"start":{"row":52,"column":66},"end":{"row":52,"column":67},"action":"insert","lines":[")"]}],[{"start":{"row":53,"column":42},"end":{"row":53,"column":43},"action":"remove","lines":["]"],"id":413},{"start":{"row":53,"column":42},"end":{"row":53,"column":43},"action":"insert","lines":[")"]}],[{"start":{"row":54,"column":52},"end":{"row":54,"column":53},"action":"remove","lines":["]"],"id":414},{"start":{"row":54,"column":52},"end":{"row":54,"column":53},"action":"insert","lines":[")"]}],[{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"remove","lines":["]"],"id":415},{"start":{"row":55,"column":54},"end":{"row":55,"column":55},"action":"insert","lines":[")"]}],[{"start":{"row":61,"column":39},"end":{"row":61,"column":57},"action":"insert","lines":[", methods=['POST']"],"id":416}],[{"start":{"row":12,"column":20},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":523},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":48,"column":0},"action":"insert","lines":["@app.route('/')","def index():","    if 'username' in session:","        return 'You are logged in as ' + session['username']","","    return render_template('index.html')","","@app.route('/login', methods=['POST'])","def login():","    users = mongo.db.users","    login_user = users.find_one({'name' : request.form['username']})","","    if login_user:","        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):","            session['username'] = request.form['username']","            return redirect(url_for('index'))","","    return 'Invalid username/password combination'","","@app.route('/register', methods=['POST', 'GET'])","def register():","    if request.method == 'POST':","        users = mongo.db.users","        existing_user = users.find_one({'name' : request.form['username']})","","        if existing_user is None:","            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())","            users.insert({'name' : request.form['username'], 'password' : hashpass})","            session['username'] = request.form['username']","            return redirect(url_for('index'))","        ","        return 'That username already exists!'","","    return render_template('register.html')",""],"id":524}],[{"start":{"row":1,"column":68},"end":{"row":1,"column":69},"action":"insert","lines":[","],"id":525}],[{"start":{"row":1,"column":69},"end":{"row":1,"column":70},"action":"insert","lines":[" "],"id":526},{"start":{"row":1,"column":70},"end":{"row":1,"column":71},"action":"insert","lines":["s"]},{"start":{"row":1,"column":71},"end":{"row":1,"column":72},"action":"insert","lines":["e"]},{"start":{"row":1,"column":72},"end":{"row":1,"column":73},"action":"insert","lines":["s"]},{"start":{"row":1,"column":73},"end":{"row":1,"column":74},"action":"insert","lines":["s"]},{"start":{"row":1,"column":74},"end":{"row":1,"column":75},"action":"insert","lines":["i"]},{"start":{"row":1,"column":75},"end":{"row":1,"column":76},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":76},"end":{"row":1,"column":77},"action":"insert","lines":["n"],"id":527},{"start":{"row":1,"column":77},"end":{"row":1,"column":78},"action":"insert","lines":[","]}],[{"start":{"row":1,"column":78},"end":{"row":1,"column":79},"action":"insert","lines":[" "],"id":528},{"start":{"row":1,"column":79},"end":{"row":1,"column":80},"action":"insert","lines":["r"]},{"start":{"row":1,"column":80},"end":{"row":1,"column":81},"action":"insert","lines":["e"]},{"start":{"row":1,"column":81},"end":{"row":1,"column":82},"action":"insert","lines":["q"]},{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"insert","lines":["w"]}],[{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"remove","lines":["w"],"id":529}],[{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"insert","lines":["u"],"id":530},{"start":{"row":1,"column":83},"end":{"row":1,"column":84},"action":"insert","lines":["e"]},{"start":{"row":1,"column":84},"end":{"row":1,"column":85},"action":"insert","lines":["s"]},{"start":{"row":1,"column":85},"end":{"row":1,"column":86},"action":"insert","lines":["t"]}],[{"start":{"row":2,"column":33},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":531}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":13},"action":"insert","lines":["import bcrypt"],"id":532}],[{"start":{"row":1,"column":85},"end":{"row":1,"column":86},"action":"remove","lines":["t"],"id":533},{"start":{"row":1,"column":84},"end":{"row":1,"column":85},"action":"remove","lines":["s"]},{"start":{"row":1,"column":83},"end":{"row":1,"column":84},"action":"remove","lines":["e"]},{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"remove","lines":["u"]},{"start":{"row":1,"column":81},"end":{"row":1,"column":82},"action":"remove","lines":["q"]},{"start":{"row":1,"column":80},"end":{"row":1,"column":81},"action":"remove","lines":["e"]},{"start":{"row":1,"column":79},"end":{"row":1,"column":80},"action":"remove","lines":["r"]},{"start":{"row":1,"column":78},"end":{"row":1,"column":79},"action":"remove","lines":[" "]},{"start":{"row":1,"column":77},"end":{"row":1,"column":78},"action":"remove","lines":[","]}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":["x"],"id":534},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"remove","lines":["e"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"remove","lines":["d"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"remove","lines":["n"]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["i"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["r"],"id":535},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["e"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["c"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["i"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["p"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"remove","lines":["x"],"id":536},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"remove","lines":["e"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"remove","lines":["d"]},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"remove","lines":["n"]},{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"remove","lines":["i"]}],[{"start":{"row":20,"column":28},"end":{"row":20,"column":29},"action":"insert","lines":["r"],"id":537},{"start":{"row":20,"column":29},"end":{"row":20,"column":30},"action":"insert","lines":["e"]},{"start":{"row":20,"column":30},"end":{"row":20,"column":31},"action":"insert","lines":["c"]},{"start":{"row":20,"column":31},"end":{"row":20,"column":32},"action":"insert","lines":["i"]},{"start":{"row":20,"column":32},"end":{"row":20,"column":33},"action":"insert","lines":["p"]},{"start":{"row":20,"column":33},"end":{"row":20,"column":34},"action":"insert","lines":["e"]},{"start":{"row":20,"column":34},"end":{"row":20,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":13},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":538}],[{"start":{"row":4,"column":0},"end":{"row":4,"column":52},"action":"insert","lines":["from werkzeug.security import generate_password_hash"],"id":539}],[{"start":{"row":4,"column":52},"end":{"row":4,"column":53},"action":"insert","lines":[","],"id":540}],[{"start":{"row":4,"column":53},"end":{"row":4,"column":54},"action":"insert","lines":[" "],"id":541},{"start":{"row":4,"column":54},"end":{"row":4,"column":55},"action":"insert","lines":["c"]},{"start":{"row":4,"column":55},"end":{"row":4,"column":56},"action":"insert","lines":["h"]},{"start":{"row":4,"column":56},"end":{"row":4,"column":57},"action":"insert","lines":["e"]},{"start":{"row":4,"column":57},"end":{"row":4,"column":58},"action":"insert","lines":["c"]},{"start":{"row":4,"column":58},"end":{"row":4,"column":59},"action":"insert","lines":["k"]}],[{"start":{"row":4,"column":59},"end":{"row":4,"column":60},"action":"insert","lines":["_"],"id":542},{"start":{"row":4,"column":60},"end":{"row":4,"column":61},"action":"insert","lines":["p"]},{"start":{"row":4,"column":61},"end":{"row":4,"column":62},"action":"insert","lines":["a"]},{"start":{"row":4,"column":62},"end":{"row":4,"column":63},"action":"insert","lines":["s"]},{"start":{"row":4,"column":63},"end":{"row":4,"column":64},"action":"insert","lines":["s"]},{"start":{"row":4,"column":64},"end":{"row":4,"column":65},"action":"insert","lines":["w"]},{"start":{"row":4,"column":65},"end":{"row":4,"column":66},"action":"insert","lines":["o"]},{"start":{"row":4,"column":66},"end":{"row":4,"column":67},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":67},"end":{"row":4,"column":68},"action":"insert","lines":["d"],"id":543},{"start":{"row":4,"column":68},"end":{"row":4,"column":69},"action":"insert","lines":["_"]},{"start":{"row":4,"column":69},"end":{"row":4,"column":70},"action":"insert","lines":["h"]},{"start":{"row":4,"column":70},"end":{"row":4,"column":71},"action":"insert","lines":["a"]},{"start":{"row":4,"column":71},"end":{"row":4,"column":72},"action":"insert","lines":["s"]},{"start":{"row":4,"column":72},"end":{"row":4,"column":73},"action":"insert","lines":["h"]}],[{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"remove","lines":["x"],"id":544},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"remove","lines":["e"]},{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"remove","lines":["d"]},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"remove","lines":["n"]},{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"remove","lines":["i"]}],[{"start":{"row":31,"column":37},"end":{"row":31,"column":38},"action":"insert","lines":["r"],"id":545},{"start":{"row":31,"column":38},"end":{"row":31,"column":39},"action":"insert","lines":["e"]}],[{"start":{"row":31,"column":39},"end":{"row":31,"column":40},"action":"insert","lines":["c"],"id":546},{"start":{"row":31,"column":40},"end":{"row":31,"column":41},"action":"insert","lines":["i"]},{"start":{"row":31,"column":41},"end":{"row":31,"column":42},"action":"insert","lines":["p"]}],[{"start":{"row":31,"column":42},"end":{"row":31,"column":43},"action":"insert","lines":["e"],"id":547},{"start":{"row":31,"column":43},"end":{"row":31,"column":44},"action":"insert","lines":["s"]}],[{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"remove","lines":["x"],"id":548},{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"remove","lines":["e"]},{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"remove","lines":["d"]},{"start":{"row":45,"column":38},"end":{"row":45,"column":39},"action":"remove","lines":["n"]},{"start":{"row":45,"column":37},"end":{"row":45,"column":38},"action":"remove","lines":["i"]}],[{"start":{"row":45,"column":37},"end":{"row":45,"column":38},"action":"insert","lines":["r"],"id":549},{"start":{"row":45,"column":38},"end":{"row":45,"column":39},"action":"insert","lines":["e"]},{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":["c"]},{"start":{"row":45,"column":40},"end":{"row":45,"column":41},"action":"insert","lines":["i"]}],[{"start":{"row":45,"column":41},"end":{"row":45,"column":42},"action":"insert","lines":["p"],"id":550},{"start":{"row":45,"column":42},"end":{"row":45,"column":43},"action":"insert","lines":["e"]},{"start":{"row":45,"column":43},"end":{"row":45,"column":44},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":0},"end":{"row":52,"column":0},"action":"remove","lines":["@app.route('/')","def recipe():","    if 'username' in session:","        return 'You are logged in as ' + session['username']","","    return render_template('recipes.html')","","@app.route('/login', methods=['POST'])","def login():","    users = mongo.db.users","    login_user = users.find_one({'name' : request.form['username']})","","    if login_user:","        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):","            session['username'] = request.form['username']","            return redirect(url_for('recipes'))","","    return 'Invalid username/password combination'","","@app.route('/register', methods=['POST', 'GET'])","def register():","    if request.method == 'POST':","        users = mongo.db.users","        existing_user = users.find_one({'name' : request.form['username']})","","        if existing_user is None:","            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())","            users.insert({'name' : request.form['username'], 'password' : hashpass})","            session['username'] = request.form['username']","            return redirect(url_for('recipes'))","        ","        return 'That username already exists!'","","    return render_template('register.html')","","",""],"id":556}],[{"start":{"row":16,"column":0},"end":{"row":106,"column":0},"action":"insert","lines":["# Login","@app.route('/login', methods=['GET'])","def login():","\t# Check if user is not logged in already","\tif 'user' in session:","\t\tuser_in_db = users_collection.find_one({\"username\": session['user']})","\t\tif user_in_db:","\t\t\t# If so redirect user to his profile","\t\t\tflash(\"You are logged in already!\")","\t\t\treturn redirect(url_for('profile', user=user_in_db['username']))","\telse:","\t\t# Render the page for user to be able to log in","\t\treturn render_template(\"login.html\")","","# Check user login details from login form","@app.route('/user_auth', methods=['POST'])","def user_auth():","\tform = request.form.to_dict()","\tuser_in_db = users_collection.find_one({\"username\": form['username']})","\t# Check for user in database","\tif user_in_db:","\t\t# If passwords match (hashed / real password)","\t\tif check_password_hash(user_in_db['password'], form['user_password']):","\t\t\t# Log user in (add to session)","\t\t\tsession['user'] = form['username']","\t\t\t# If the user is admin redirect him to admin area","\t\t\tif session['user'] == \"admin\":","\t\t\t\treturn redirect(url_for('admin'))","\t\t\telse:","\t\t\t\tflash(\"You were logged in!\")","\t\t\t\treturn redirect(url_for('profile', user=user_in_db['username']))","\t\t\t","\t\telse:","\t\t\tflash(\"Wrong password or user name!\")","\t\t\treturn redirect(url_for('login'))","\telse:","\t\tflash(\"You must be registered!\")","\t\treturn redirect(url_for('register'))","","# Sign up","@app.route('/register', methods=['GET', 'POST'])","def register():","\t# Check if user is not logged in already","\tif 'user' in session:","\t\tflash('You are already sign in!')","\t\treturn redirect(url_for('index'))","\tif request.method == 'POST':","\t\tform = request.form.to_dict()","\t\t# Check if the password and password1 actualy match ","\t\tif form['user_password'] == form['user_password1']:","\t\t\t# If so try to find the user in db","\t\t\tuser = users_collection.find_one({\"username\" : form['username']})","\t\t\tif user:","\t\t\t\tflash(f\"{form['username']} already exists!\")","\t\t\t\treturn redirect(url_for('register'))","\t\t\t# If user does not exist register new user","\t\t\telse:\t\t\t\t","\t\t\t\t# Hash password","\t\t\t\thash_pass = generate_password_hash(form['user_password'])","\t\t\t\t#Create new user with hashed password","\t\t\t\tusers_collection.insert_one(","\t\t\t\t\t{","\t\t\t\t\t\t'username': form['username'],","\t\t\t\t\t\t'email': form['email'],","\t\t\t\t\t\t'password': hash_pass","\t\t\t\t\t}","\t\t\t\t)","\t\t\t\t# Check if user is actualy saved","\t\t\t\tuser_in_db = users_collection.find_one({\"username\": form['username']})","\t\t\t\tif user_in_db:","\t\t\t\t\t# Log user in (add to session)","\t\t\t\t\tsession['user'] = user_in_db['username']","\t\t\t\t\treturn redirect(url_for('profile', user=user_in_db['username']))","\t\t\t\telse:","\t\t\t\t\tflash(\"There was a problem savaing your profile\")","\t\t\t\t\treturn redirect(url_for('register'))","","\t\telse:","\t\t\tflash(\"Passwords dont match!\")","\t\t\treturn redirect(url_for('register'))","\t\t","\treturn render_template(\"register.html\")","","# Log out","@app.route('/logout')","def logout():","\t# Clear the session","\tsession.clear()","\tflash('You were logged out!')","\treturn redirect(url_for('index'))",""],"id":557}],[{"start":{"row":1,"column":77},"end":{"row":1,"column":78},"action":"insert","lines":[","],"id":558}],[{"start":{"row":1,"column":78},"end":{"row":1,"column":79},"action":"insert","lines":[" "],"id":559},{"start":{"row":1,"column":79},"end":{"row":1,"column":80},"action":"insert","lines":["f"]},{"start":{"row":1,"column":80},"end":{"row":1,"column":81},"action":"insert","lines":["l"]},{"start":{"row":1,"column":81},"end":{"row":1,"column":82},"action":"insert","lines":["a"]},{"start":{"row":1,"column":82},"end":{"row":1,"column":83},"action":"insert","lines":["s"]},{"start":{"row":1,"column":83},"end":{"row":1,"column":84},"action":"insert","lines":["h"]}],[{"start":{"row":14,"column":20},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":560}],[{"start":{"row":15,"column":0},"end":{"row":18,"column":37},"action":"insert","lines":["# Collections","","users_collection = mongo.db.users","recipes_collection = mongo.db.recipes"],"id":561}],[{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":562}],[{"start":{"row":36,"column":0},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":563}],[{"start":{"row":58,"column":16},"end":{"row":58,"column":17},"action":"remove","lines":["t"],"id":564},{"start":{"row":58,"column":15},"end":{"row":58,"column":16},"action":"remove","lines":["s"]},{"start":{"row":58,"column":14},"end":{"row":58,"column":15},"action":"remove","lines":["u"]},{"start":{"row":58,"column":13},"end":{"row":58,"column":14},"action":"remove","lines":["m"]}],[{"start":{"row":58,"column":13},"end":{"row":58,"column":14},"action":"insert","lines":["n"],"id":565},{"start":{"row":58,"column":14},"end":{"row":58,"column":15},"action":"insert","lines":["e"]},{"start":{"row":58,"column":15},"end":{"row":58,"column":16},"action":"insert","lines":["e"]},{"start":{"row":58,"column":16},"end":{"row":58,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":58,"column":17},"end":{"row":58,"column":18},"action":"insert","lines":[" "],"id":566},{"start":{"row":58,"column":18},"end":{"row":58,"column":19},"action":"insert","lines":["t"]},{"start":{"row":58,"column":19},"end":{"row":58,"column":20},"action":"insert","lines":["o"]},{"start":{"row":58,"column":20},"end":{"row":58,"column":21},"action":"insert","lines":[" "]},{"start":{"row":58,"column":21},"end":{"row":58,"column":22},"action":"insert","lines":["s"]},{"start":{"row":58,"column":22},"end":{"row":58,"column":23},"action":"insert","lines":["i"]},{"start":{"row":58,"column":23},"end":{"row":58,"column":24},"action":"insert","lines":["g"]}],[{"start":{"row":58,"column":24},"end":{"row":58,"column":25},"action":"insert","lines":["n"],"id":567},{"start":{"row":58,"column":25},"end":{"row":58,"column":26},"action":"insert","lines":["u"]},{"start":{"row":58,"column":26},"end":{"row":58,"column":27},"action":"insert","lines":["p"]}],[{"start":{"row":58,"column":28},"end":{"row":58,"column":41},"action":"remove","lines":["be registered"],"id":568}],[{"start":{"row":70,"column":46},"end":{"row":70,"column":47},"action":"insert","lines":["l"],"id":569}],[{"start":{"row":66,"column":9},"end":{"row":66,"column":18},"action":"remove","lines":["You are a"],"id":570},{"start":{"row":66,"column":9},"end":{"row":66,"column":10},"action":"insert","lines":["A"]}],[{"start":{"row":67,"column":27},"end":{"row":67,"column":32},"action":"remove","lines":["index"],"id":571},{"start":{"row":67,"column":27},"end":{"row":67,"column":28},"action":"insert","lines":["r"]},{"start":{"row":67,"column":28},"end":{"row":67,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":67,"column":29},"end":{"row":67,"column":30},"action":"insert","lines":["c"],"id":572},{"start":{"row":67,"column":30},"end":{"row":67,"column":31},"action":"insert","lines":["i"]},{"start":{"row":67,"column":31},"end":{"row":67,"column":32},"action":"insert","lines":["p"]},{"start":{"row":67,"column":32},"end":{"row":67,"column":33},"action":"insert","lines":["e"]},{"start":{"row":67,"column":33},"end":{"row":67,"column":34},"action":"insert","lines":["s"]}],[{"start":{"row":85,"column":6},"end":{"row":85,"column":29},"action":"remove","lines":["'email': form['email'],"],"id":573},{"start":{"row":85,"column":5},"end":{"row":85,"column":6},"action":"remove","lines":["\t"]},{"start":{"row":85,"column":4},"end":{"row":85,"column":5},"action":"remove","lines":["\t"]},{"start":{"row":85,"column":3},"end":{"row":85,"column":4},"action":"remove","lines":["\t"]},{"start":{"row":85,"column":2},"end":{"row":85,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":85,"column":1},"end":{"row":85,"column":2},"action":"remove","lines":["\t"]}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"remove","lines":["\t"],"id":574},{"start":{"row":84,"column":35},"end":{"row":85,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":88,"column":28},"end":{"row":88,"column":29},"action":"insert","lines":["l"],"id":575}],[{"start":{"row":95,"column":35},"end":{"row":95,"column":36},"action":"remove","lines":["a"],"id":576}],[{"start":{"row":99,"column":23},"end":{"row":99,"column":24},"action":"insert","lines":["'"],"id":577}],[{"start":{"row":102,"column":37},"end":{"row":102,"column":38},"action":"remove","lines":["l"],"id":578},{"start":{"row":102,"column":36},"end":{"row":102,"column":37},"action":"remove","lines":["m"]},{"start":{"row":102,"column":35},"end":{"row":102,"column":36},"action":"remove","lines":["t"]},{"start":{"row":102,"column":34},"end":{"row":102,"column":35},"action":"remove","lines":["h"]},{"start":{"row":102,"column":33},"end":{"row":102,"column":34},"action":"remove","lines":["."]}],[{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"remove","lines":["x"],"id":579},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"remove","lines":["e"]},{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"remove","lines":["d"]},{"start":{"row":110,"column":27},"end":{"row":110,"column":28},"action":"remove","lines":["n"]},{"start":{"row":110,"column":26},"end":{"row":110,"column":27},"action":"remove","lines":["i"]}],[{"start":{"row":110,"column":26},"end":{"row":110,"column":27},"action":"insert","lines":["r"],"id":580},{"start":{"row":110,"column":27},"end":{"row":110,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":110,"column":28},"end":{"row":110,"column":29},"action":"insert","lines":["c"],"id":581},{"start":{"row":110,"column":29},"end":{"row":110,"column":30},"action":"insert","lines":["i"]},{"start":{"row":110,"column":30},"end":{"row":110,"column":31},"action":"insert","lines":["p"]},{"start":{"row":110,"column":31},"end":{"row":110,"column":32},"action":"insert","lines":["e"]},{"start":{"row":110,"column":32},"end":{"row":110,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":35},"end":{"row":33,"column":36},"action":"remove","lines":["l"],"id":582},{"start":{"row":33,"column":34},"end":{"row":33,"column":35},"action":"remove","lines":["m"]},{"start":{"row":33,"column":33},"end":{"row":33,"column":34},"action":"remove","lines":["t"]},{"start":{"row":33,"column":32},"end":{"row":33,"column":33},"action":"remove","lines":["h"]},{"start":{"row":33,"column":31},"end":{"row":33,"column":32},"action":"remove","lines":["."]}],[{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"remove","lines":["n"],"id":583},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"remove","lines":["i"]},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"remove","lines":["g"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"remove","lines":["o"]},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"remove","lines":["l"]}],[{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["r"],"id":584},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["e"]},{"start":{"row":33,"column":28},"end":{"row":33,"column":29},"action":"insert","lines":["c"]},{"start":{"row":33,"column":29},"end":{"row":33,"column":30},"action":"insert","lines":["i"]}],[{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"insert","lines":["p"],"id":585},{"start":{"row":33,"column":31},"end":{"row":33,"column":32},"action":"insert","lines":["e"]},{"start":{"row":33,"column":32},"end":{"row":33,"column":33},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":33},"end":{"row":33,"column":34},"action":"insert","lines":["."],"id":586},{"start":{"row":33,"column":34},"end":{"row":33,"column":35},"action":"insert","lines":["h"]},{"start":{"row":33,"column":35},"end":{"row":33,"column":36},"action":"insert","lines":["t"]},{"start":{"row":33,"column":36},"end":{"row":33,"column":37},"action":"insert","lines":["m"]},{"start":{"row":33,"column":37},"end":{"row":33,"column":38},"action":"insert","lines":["l"]}],[{"start":{"row":24,"column":24},"end":{"row":24,"column":33},"action":"remove","lines":["logged in"],"id":587}],[{"start":{"row":24,"column":23},"end":{"row":24,"column":24},"action":"remove","lines":[" "],"id":588}],[{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":[" "],"id":589}],[{"start":{"row":24,"column":32},"end":{"row":24,"column":41},"action":"insert","lines":["logged in"],"id":590}],[{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"remove","lines":[" "],"id":591}],[{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":[" "],"id":592}],[{"start":{"row":28,"column":28},"end":{"row":28,"column":39},"action":"remove","lines":["his profile"],"id":593},{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"insert","lines":["m"]},{"start":{"row":28,"column":29},"end":{"row":28,"column":30},"action":"insert","lines":["a"]},{"start":{"row":28,"column":30},"end":{"row":28,"column":31},"action":"insert","lines":["i"]},{"start":{"row":28,"column":31},"end":{"row":28,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":28,"column":32},"end":{"row":28,"column":33},"action":"insert","lines":[" "],"id":594},{"start":{"row":28,"column":33},"end":{"row":28,"column":34},"action":"insert","lines":["p"]},{"start":{"row":28,"column":34},"end":{"row":28,"column":35},"action":"insert","lines":["a"]},{"start":{"row":28,"column":35},"end":{"row":28,"column":36},"action":"insert","lines":["g"]},{"start":{"row":28,"column":36},"end":{"row":28,"column":37},"action":"insert","lines":["e"]}],[{"start":{"row":30,"column":28},"end":{"row":30,"column":35},"action":"remove","lines":["profile"],"id":595},{"start":{"row":30,"column":28},"end":{"row":30,"column":29},"action":"insert","lines":["r"]},{"start":{"row":30,"column":29},"end":{"row":30,"column":30},"action":"insert","lines":["e"]},{"start":{"row":30,"column":30},"end":{"row":30,"column":31},"action":"insert","lines":["c"]},{"start":{"row":30,"column":31},"end":{"row":30,"column":32},"action":"insert","lines":["i"]},{"start":{"row":30,"column":32},"end":{"row":30,"column":33},"action":"insert","lines":["p"]},{"start":{"row":30,"column":33},"end":{"row":30,"column":34},"action":"insert","lines":["e"]},{"start":{"row":30,"column":34},"end":{"row":30,"column":35},"action":"insert","lines":["s"]}],[{"start":{"row":52,"column":29},"end":{"row":52,"column":36},"action":"remove","lines":["profile"],"id":596},{"start":{"row":52,"column":29},"end":{"row":52,"column":30},"action":"insert","lines":["r"]},{"start":{"row":52,"column":30},"end":{"row":52,"column":31},"action":"insert","lines":["e"]},{"start":{"row":52,"column":31},"end":{"row":52,"column":32},"action":"insert","lines":["c"]},{"start":{"row":52,"column":32},"end":{"row":52,"column":33},"action":"insert","lines":["i"]},{"start":{"row":52,"column":33},"end":{"row":52,"column":34},"action":"insert","lines":["p"]},{"start":{"row":52,"column":34},"end":{"row":52,"column":35},"action":"insert","lines":["e"]},{"start":{"row":52,"column":35},"end":{"row":52,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":26},"end":{"row":48,"column":31},"action":"remove","lines":["admin"],"id":597},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"insert","lines":["u"]},{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"insert","lines":["s"]},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"insert","lines":["e"]},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["r"]}],[{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"remove","lines":["n"],"id":601},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"remove","lines":["i"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"remove","lines":["m"]},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"remove","lines":["d"]},{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"remove","lines":["a"]}],[{"start":{"row":49,"column":29},"end":{"row":49,"column":30},"action":"insert","lines":["r"],"id":602},{"start":{"row":49,"column":30},"end":{"row":49,"column":31},"action":"insert","lines":["e"]},{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":["c"]},{"start":{"row":49,"column":32},"end":{"row":49,"column":33},"action":"insert","lines":["i"]},{"start":{"row":49,"column":33},"end":{"row":49,"column":34},"action":"insert","lines":["p"]}],[{"start":{"row":49,"column":34},"end":{"row":49,"column":35},"action":"insert","lines":["e"],"id":603},{"start":{"row":49,"column":35},"end":{"row":49,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":116,"column":36},"end":{"row":117,"column":0},"action":"insert","lines":["",""],"id":604},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"insert","lines":["    "]},{"start":{"row":117,"column":4},"end":{"row":118,"column":0},"action":"insert","lines":["",""]},{"start":{"row":118,"column":0},"end":{"row":118,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":118,"column":3},"end":{"row":118,"column":4},"action":"remove","lines":[" "],"id":605},{"start":{"row":118,"column":2},"end":{"row":118,"column":3},"action":"remove","lines":[" "]},{"start":{"row":118,"column":1},"end":{"row":118,"column":2},"action":"remove","lines":[" "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":118,"column":0},"end":{"row":121,"column":36},"action":"insert","lines":["@app.route('/get_recipes')","def get_recipes():","    return render_template(\"recipes.html\", ","    recipes=mongo.db.recipes.find())"],"id":606}],[{"start":{"row":118,"column":23},"end":{"row":118,"column":24},"action":"remove","lines":["s"],"id":607},{"start":{"row":118,"column":22},"end":{"row":118,"column":23},"action":"remove","lines":["e"]},{"start":{"row":118,"column":21},"end":{"row":118,"column":22},"action":"remove","lines":["p"]},{"start":{"row":118,"column":20},"end":{"row":118,"column":21},"action":"remove","lines":["i"]},{"start":{"row":118,"column":19},"end":{"row":118,"column":20},"action":"remove","lines":["c"]},{"start":{"row":118,"column":18},"end":{"row":118,"column":19},"action":"remove","lines":["e"]},{"start":{"row":118,"column":17},"end":{"row":118,"column":18},"action":"remove","lines":["r"]},{"start":{"row":118,"column":16},"end":{"row":118,"column":17},"action":"remove","lines":["_"]},{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"remove","lines":["t"]},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"remove","lines":["e"]}],[{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"remove","lines":["g"],"id":608}],[{"start":{"row":118,"column":13},"end":{"row":118,"column":14},"action":"insert","lines":["s"],"id":609},{"start":{"row":118,"column":14},"end":{"row":118,"column":15},"action":"insert","lines":["t"]},{"start":{"row":118,"column":15},"end":{"row":118,"column":16},"action":"insert","lines":["a"]},{"start":{"row":118,"column":16},"end":{"row":118,"column":17},"action":"insert","lines":["t"]},{"start":{"row":118,"column":17},"end":{"row":118,"column":18},"action":"insert","lines":["s"]}],[{"start":{"row":119,"column":14},"end":{"row":119,"column":15},"action":"remove","lines":["s"],"id":610},{"start":{"row":119,"column":13},"end":{"row":119,"column":14},"action":"remove","lines":["e"]},{"start":{"row":119,"column":12},"end":{"row":119,"column":13},"action":"remove","lines":["p"]},{"start":{"row":119,"column":11},"end":{"row":119,"column":12},"action":"remove","lines":["i"]},{"start":{"row":119,"column":10},"end":{"row":119,"column":11},"action":"remove","lines":["c"]},{"start":{"row":119,"column":9},"end":{"row":119,"column":10},"action":"remove","lines":["e"]},{"start":{"row":119,"column":8},"end":{"row":119,"column":9},"action":"remove","lines":["r"]},{"start":{"row":119,"column":7},"end":{"row":119,"column":8},"action":"remove","lines":["_"]},{"start":{"row":119,"column":6},"end":{"row":119,"column":7},"action":"remove","lines":["t"]}],[{"start":{"row":119,"column":5},"end":{"row":119,"column":6},"action":"remove","lines":["e"],"id":611},{"start":{"row":119,"column":4},"end":{"row":119,"column":5},"action":"remove","lines":["g"]}],[{"start":{"row":119,"column":4},"end":{"row":119,"column":5},"action":"insert","lines":["s"],"id":612},{"start":{"row":119,"column":5},"end":{"row":119,"column":6},"action":"insert","lines":["t"]},{"start":{"row":119,"column":6},"end":{"row":119,"column":7},"action":"insert","lines":["a"]},{"start":{"row":119,"column":7},"end":{"row":119,"column":8},"action":"insert","lines":["t"]},{"start":{"row":119,"column":8},"end":{"row":119,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":120,"column":28},"end":{"row":120,"column":34},"action":"remove","lines":["recipe"],"id":613}],[{"start":{"row":120,"column":28},"end":{"row":120,"column":29},"action":"insert","lines":["s"],"id":614},{"start":{"row":120,"column":29},"end":{"row":120,"column":30},"action":"insert","lines":["t"]},{"start":{"row":120,"column":30},"end":{"row":120,"column":31},"action":"insert","lines":["a"]},{"start":{"row":120,"column":31},"end":{"row":120,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":120,"column":31},"end":{"row":120,"column":32},"action":"remove","lines":["s"],"id":615}],[{"start":{"row":120,"column":31},"end":{"row":120,"column":32},"action":"insert","lines":["t"],"id":616}],[{"start":{"row":55,"column":32},"end":{"row":55,"column":33},"action":"remove","lines":[" "],"id":622}],[{"start":{"row":44,"column":59},"end":{"row":44,"column":60},"action":"remove","lines":["_"],"id":623},{"start":{"row":44,"column":58},"end":{"row":44,"column":59},"action":"remove","lines":["r"]},{"start":{"row":44,"column":57},"end":{"row":44,"column":58},"action":"remove","lines":["e"]},{"start":{"row":44,"column":56},"end":{"row":44,"column":57},"action":"remove","lines":["s"]},{"start":{"row":44,"column":55},"end":{"row":44,"column":56},"action":"remove","lines":["u"]}],[{"start":{"row":71,"column":15},"end":{"row":71,"column":16},"action":"remove","lines":["_"],"id":624},{"start":{"row":71,"column":14},"end":{"row":71,"column":15},"action":"remove","lines":["r"]},{"start":{"row":71,"column":13},"end":{"row":71,"column":14},"action":"remove","lines":["e"]},{"start":{"row":71,"column":12},"end":{"row":71,"column":13},"action":"remove","lines":["s"]},{"start":{"row":71,"column":11},"end":{"row":71,"column":12},"action":"remove","lines":["u"]}],[{"start":{"row":71,"column":35},"end":{"row":71,"column":36},"action":"remove","lines":["_"],"id":625},{"start":{"row":71,"column":34},"end":{"row":71,"column":35},"action":"remove","lines":["r"]},{"start":{"row":71,"column":33},"end":{"row":71,"column":34},"action":"remove","lines":["e"]},{"start":{"row":71,"column":32},"end":{"row":71,"column":33},"action":"remove","lines":["s"]},{"start":{"row":71,"column":31},"end":{"row":71,"column":32},"action":"remove","lines":["u"]}],[{"start":{"row":80,"column":49},"end":{"row":80,"column":50},"action":"remove","lines":["_"],"id":626},{"start":{"row":80,"column":48},"end":{"row":80,"column":49},"action":"remove","lines":["r"]},{"start":{"row":80,"column":47},"end":{"row":80,"column":48},"action":"remove","lines":["e"]},{"start":{"row":80,"column":46},"end":{"row":80,"column":47},"action":"remove","lines":["s"]},{"start":{"row":80,"column":45},"end":{"row":80,"column":46},"action":"remove","lines":["u"]}]]},"ace":{"folds":[],"scrolltop":1346,"scrollleft":0,"selection":{"start":{"row":117,"column":4},"end":{"row":117,"column":4},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":95,"state":"start","mode":"ace/mode/python"}},"timestamp":1582299987040,"hash":"dfee2ff1f930b4e42e46172fb7dc9cf9a340f8bb"}