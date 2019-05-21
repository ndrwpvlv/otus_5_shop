# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# APP
app = Flask(__name__)
app.config.from_object('config.DevelopConfig')
db = SQLAlchemy(app)

from shop.handlers import Index
from shop import views
