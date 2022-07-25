
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