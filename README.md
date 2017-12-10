# Guess
A Flask version of guess the number game via [Hello Flask](https://github.com/helloflask/guess)

## Demo
[Guess The Number](http://hit-game.herokuapp.com/)

![guess](https://img.pawoo.net/media_attachments/files/004/324/296/original/2030312608b0e7d1.png)

## Versions
Python==2.7.14

Flask==0.12.2  
Flask-Bootstrap==3.3.7.1  
Flask-WTF==0.14.2  
Jinja2==2.10  
Werkzeug==0.13  
WTForms==2.1

## Installation
First, clone it from Github:
```
$ git clone git@github.com:zreox/guess.git
$ cd guess
```

Then use `pip` to install requirements (recommend to use `virtualenv` create a virtual enviroment)：
```
$ pip install -r requirements.txt
```

Run the app:
```
# Windows
$ set FLASK_APP=guess.py
# Linux
$ export FLASK_APP=guess.py

$ flask run
```

Now Go to [Play Game](http://127.0.0.1:5000/)