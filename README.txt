The Sports Catalog
==================================
Version: 1.1
----------------------------------

This is a website of my favorie sport items

--------------------------------------------

What's Included:
 - database_setup.py --> Creates the classes of User, Category, and CatalogItem for your catalog website to work correctly.
 - lotsofcategories.py --> Has sample catalog items to fill in your website.
 - application.py --> What runs the application - has all the routing, definitions, and authorization.
 - fb_client_secrets
 ================
 - templates folder --> has all the page templates which is dynamically displayed.
 - static folder --> has all css, js, images, and fonts that the program needs.

---------------------------------------------------------------------------------

How to Run:
 1) Download the vagrant config files in the directory folder you downloaded.
     - You'll also want to  install flask, sqlalchemy, requests, and oauth2client from your shell by typing:
	- pip install flask
	- pip install sqlalchemy
	- pip install requests
	- pip install oauth2client
 2) You'll also need to setup your own facebook developer account and set up your own client and secret id.
     a) Go to https://developers.facebook.com/
     b) Add new app from 'Website'
     c) Next, go through the directions and find out your App ID and App Secret ID
     d) Open up the file, 'fb_client_secrets.json' and add the two IDs there.
     e) Also in login.html (under templates), insert your App ID on line 14 & 26 where it says, 'YOUR-ID-HERE'.
 2) Open up your Git shell to the folder you unzipped this pacakge in. 
 3) Type 'vagrant up' in the shell
 4) Type 'vagrant ssh' in the shell
 5) Next, you'll have need to run the following files in order:
	1 - database_setup.py --> in your shell type, "python database_setup.py"
	2 - lotsofcategories.py --> in your shell type, "python lotsofcategories.py" (if it worked, it should say, "added catalog items!"
	3 - application.py --> like the others, type this in your shell, "python application.py". (if it worked, it should say, "Running on..." your localhost port 5000)
 6) You may now go to your web-browser and view the website.

---------------------------------------------------------------------------------

APIs - 3 API Endpoints to view Catalog information.

 1) /category/category_id/JSON --> shows all the items within the specific category ID
 2) /category/category_id/item/item_id/JSON --> shows the specific information just for the item
 3) /categories/JSON --> Shows all the categories with their IDs
