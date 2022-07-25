
# AMCEF API MicroService Python 

It is important to have either running or setup database firstly. 
I have tested Postgresql14 with pgAdmin4 where I created simple database
with name amcefsql and password 'supersecretpass' and root user is postgres.

### Screenshot of creating database

![App Screenshot](https://i.imgur.com/cFc4X8r.png)


## Understanding and running the code

You can run whole app within Python 3.9 with standard main, no need for 
any commands to run the application. Whole application is within Flask
folder, where you can run and build app.py. Whole code apart from
HTML is within app.py (main class included). After running app.py within
correctly turned on database output should like this:

### Successfully started code
![Successfully started code](https://i.imgur.com/jascNjG.png)

Basic button interface on localhost (127.0.0.1:5000) offers you only one button click on

### Button
![Button](https://i.imgur.com/BiqbVt4.png)

### After clicking button POST method interface is presented
![Interface](https://i.imgur.com/aAoV3VR.png)

This is everything you need for first setup and you can start using. However,
I recommend using a Postman to test POST, DELETE, GET, PATCH and other kind 
of requests as my interface only supports POST and GET ones.

### Understading endpoints

Multiple common scenarions are projected in AMCEF.postman_collection.json that can be
imported to Postman that supports wide testing of HTTP requests. 

### Endpoint 1 - Creating a post 

#### ENDPOINT 

/postadd

#### BODY (example)
{\
&nbsp;    "userId"  : 1\
&nbsp;    "title"   : "Title"\
 &nbsp;   "body"    : "LoremIpsum"  \
}

#### METHOD 
POST

#### DESCRIPTION 
Endpoint offering possibility to create / post new posts to the database.

### Endpoint 2a - Search a post based on its own id

#### ENDPOINT 

/postid/idx

#### BODY (example)
None

#### METHOD 
GET

#### DESCRIPTION 
Endpoint offering possibility to get or read external API or own database
and search for desired post with id (marked as idx).

### Endpoint 2b - Search a post based on its owner id

#### ENDPOINT 

/postbyuser/idx

#### BODY (example)
None

#### METHOD 
GET

#### DESCRIPTION 
Endpoint offering possibility to get or read own database
and search for all desired posts with userId matching the posts
 (marked as idx).

### Endpoint 3 - Delete a post based on its id

#### ENDPOINT 

/deletepost/idx

#### BODY (example)
None

#### METHOD 
DELETE

#### DESCRIPTION 
Endpoint offering possibility to delete post within own database
matching the post (marked as idx). If it does not exist in database
and it will search for it within external API that cannot be removed,
it will still return a success. However there is nothing you can really do.

### Endpoint 4 - Patch a post based on its id

#### ENDPOINT 

/editpost/idx

#### BODY (example)
{\
&nbsp;    "anything"  : "anything" \
&nbsp;    "title"     : "New title" \
&nbsp;    "body"      : "New Lorem Ipsum" \
}

#### METHOD 
PATCH

#### DESCRIPTION 
Endpoint will replace all posts within database, meaning loaded posts from external API and database only posts.
It will replace only title and body part, wont interact with userId or won't add anything other attribute.