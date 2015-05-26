from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User

#New imports for this step
from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

#Connect to Database and create database session
engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE = state)

####insert FB connect stuff#####
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.3/me"
    # strip expire tag from access token
    token = result.split("&")[0]


    url = 'https://graph.facebook.com/v2.3/me?%s' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.3/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output

# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

######insert FB Disconnect###########
@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s%s/permissions' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


#JSON APIs to view Category Information
@app.route('/category/<int:category_id>/JSON')
def categoryItemJSON(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(CatalogItem).filter_by(category_id = category_id).all()
    return jsonify(CategoryItems = [i.serialize for i in items])


@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def menuItemJSON(category_id, item_id):
    Category_Item = session.query(CatalogItem).filter_by(id = item_id).one()
    return jsonify(Category_Item = Category_Item.serialize)

@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories= [r.serialize for r in categories])


#Show all categories and some items on home page
@app.route('/')
@app.route('/categories/')
def showCategories():
  categories = session.query(Category).order_by(asc(Category.name))
  category = session.query(Category).order_by(Category.name).all()
  catalog_items = session.query(CatalogItem).order_by(CatalogItem.category_id).order_by(CatalogItem.title).all()
  return render_template('categories.html', categories = categories, category = category, catalog_items = catalog_items)

#Show all items within the specified category
@app.route('/category/<int:category_id>/')
def showCategoryItems(category_id):
  category = session.query(Category).filter_by(id = category_id).one()
  creator = getUserInfo(category.user_id)
  catalog_items = session.query(CatalogItem).filter_by(category_id = category_id).all()
  if 'username' not in login_session or creator.id != login_session['user_id']:
    return render_template('publiccategory.html', catalog_items = catalog_items, category = category, creator = creator)
  else:
    return render_template('category.html', catalog_items = catalog_items, category = category, creator = creator)

#Shows the specific item within the category
@app.route('/category/<int:category_id>/item/<int:item_id>/')
def showCategoryItem(category_id, item_id):
  category = session.query(Category).filter_by(id = category_id).one()
  category_item = session.query(CatalogItem).filter_by(id = item_id).one()
  if 'username' not in login_session:
    return render_template('publiccategoryItem.html', category = category, category_item = category_item)
  else:
    return render_template('categoryItem.html', category = category, category_item = category_item)

#edits the specific category item
@app.route('/category/<int:category_id>/item/<int:item_id>/edit/', methods = ['GET', 'POST'])
def editCategoryItem(category_id, item_id):
    if 'username' not in login_session:
      return redirect('/login')
    category = session.query(Category).filter_by(id = category_id).one()
    editedItem = session.query(CatalogItem).filter_by(id = item_id).one()
    if request.method == 'POST':
        if request.form['title']:
            editedItem.title = request.form['title']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['item_picture']:
            editedItem.item_picture = request.form['item_picture']
        session.add(editedItem)
        session.commit()
        flash('Item %s Was Successfully Edited!' % (editedItem.title)) 
        return redirect(url_for('showCategoryItems', category_id = category_id))
    else:
        return render_template('editCategoryItem.html', category_id = category_id, item_id = item_id, item = editedItem)

#delete the specific category item
@app.route('/category/<int:category_id>/item/<int:item_id>/delete/', methods = ['GET','POST'])
def deleteCategoryItem(category_id, item_id):
    #category = session.query(Category).filter_by(id = category_id).one()
    if 'username' not in login_session:
      return redirect('/login')
    itemToDelete = session.query(CatalogItem).filter_by(id = item_id).one() 
    if itemToDelete.user_id != login_session['user_id']:
      return "<script>function myFunction() {alert('You are not authorized to delete this item. Please create your own item in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item %s Was Successfully Deleted!' % (itemToDelete.title))
        return redirect(url_for('showCategoryItems', category_id = category_id))
    else:
        return render_template('deleteCategoryItem.html', item = itemToDelete)

#create new category item
@app.route('/category/<int:category_id>/new/', methods=['GET','POST'])
def newCategoryItem(category_id):
  if 'username' not in login_session:
    return redirect('/login')
  category = session.query(Category).filter_by(id = category_id).one()
  if request.method == 'POST':
      newItem = CatalogItem(title = request.form['title'], description = request.form['description'], price = request.form['price'], item_picture = request.form['item_picture'], category_id = category_id, user_id = category.user_id)
      session.add(newItem)
      session.commit()
      flash('New Item %s Was Successfully Created!' % (newItem.title))
      return redirect(url_for('showCategoryItems', category_id = category_id))
  else:
      return render_template('newCategoryItem.html', category_id = category_id)

# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCategories'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCategories'))

if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 5000)
