# code_syntax_analyser

**otus_5_shop** - fourth homework of OTUS Python course - Training to make online store with Flask wsgi framework and etc.

Homework-shop based on Flask, Jinja2, Werkzeug and SQLAlchemy.

Now it demonstrate index, catalog and products pages only. 

## Installation
Download source or clone this repository. For run you need uWSGI server installed.

## Before start
First you need to organize virtual environment with requirements.txt.

Second you need to make database and fill it with some data by create_db.py file. From repository directory run: 
```
python3 -m create_db
```

## Basic usage
For running server under uWSGI you can find in repository shop.ini. Run it with terminal:
```
uwsgi shop.ini
```
Before run application edit shop.ini. Update home, wsgi-file, virtualenv variables. 
```
[uwsgi]
plugin = python3
http = 127.0.0.1:5000
processes = 1
home = /home/path/otus_5_shop
wsgi-file = /home/path/otus_5_shop/shop
virtualenv = /home/path/venv/otus_5_shop
stats = 127.0.0.1:9191
module = shop:app
```

Other way to run dev server is to use included in Flask/Werkzeug wsgi dev server. From terminal from repository directory run:
```
python3 -m run
```


## Requirements
```
Python 3.5+

Click==7.0
Flask==1.0.3
Flask-SQLAlchemy==2.4.0
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
SQLAlchemy==1.3.3
Werkzeug==0.15.4
```

## Contributors
Andrei S. Pavlov (https://github.com/ndrwpvlv/)
