{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":102,"column":0},"end":{"row":135,"column":4},"action":"remove","lines":["def get_recipes(offset=0, per_page=3):","\trecipes = mongo.db.recipes.find()","\tprint (\"herl\")","\treturn recipes[offset:offset + per_page]","\t","@app.route('get_recipes')","def showRecipes():","\tpage, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')","\ttotal = mong.db.recipes.find()","","","\tdef get_recipes(offset=0, per_page=3):","\t  recipes = mongo.db.recipes.find()","\tprint(\"herl\")","\treturn recipes[offset: offset + per_page]","@app.route('/get_recipes')","\t","def showRecipes():","    page, per_page, offset = get_page_args(page_parameter='page',","\tper_page_parameter='per_page'),","total = mongo.db.recipes.find().count()","paginatedRecipes = get_recipes(offset=offset, per_page=per_page)","pagination = Pagination(page=page, per_page=per_page, total=total,","\t             css_framework='bootstrap4')",""," ","return render_template('recipes.html',","\t\t   recipes=paginatedRecipes,","           page=page,","           per_page=per_page,","           pagination=pagination,","                                 )","","    "],"id":2292},{"start":{"row":102,"column":0},"end":{"row":127,"column":45},"action":"insert","lines":["@app.route('/', defaults = {'page_no': 0})","@app.route('/get_recipes/<page_no>', defaults = {'page_no': 0} )","def get_recipes(page_no):","\tpagination_object = None","\trecipe = mongo.db.recipes","\toffset = page_no","\tlimit = 2","\tstarting_id = recipe.find().sort('_id', pymongo.ASCENDING)","\tlast_id = starting_id[offset]['_id']","\trecipe = recipe.find({'_id' : {'$gte' : last_id}}).sort('_id', pymongo.ASCENDING).limit(limit)","\toutput = []","\tfor i in recipe:","\t\tprint(i)","\t\toutput.append(i)","\tnext_url = '/recipe?limit=' + str(limit) + '&offset=' + str(offset + limit)","\tprev_url = '/recipe?limit=' + str(limit) + '&offset=' + str(offset - limit)","\tpagination_object = ({'result' : output, 'prev_url' : prev_url, 'next_url': next_url})","\tif 'user' in session:","\t\treturn render_template(\"recipes.html\", ","\t\t\t\t\t\t\t   pagination_object=pagination_object,","\t\t\t\t\t\t\t   recipes=mongo.db.recipes.find(),","\t\t\t\t\t\t\t   user = session['user'])","\telse:\t","\t\treturn render_template(\"recipes.html\",","\t\t\t\t\t\t\t   pagination_object=pagination_object,","\t\t\t\t\t\t\t   recipes=mongo.db.recipes.find())   "]}]]},"ace":{"folds":[],"scrolltop":1743,"scrollleft":0,"selection":{"start":{"row":107,"column":17},"end":{"row":107,"column":17},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":115,"state":"start","mode":"ace/mode/python"}},"timestamp":1588703716719,"hash":"f1d8062e04a532fd8adb92aab3c898f619698512"}