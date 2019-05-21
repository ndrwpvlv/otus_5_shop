# -*- coding: utf-8 -*-

import os
from datetime import timedelta

# PATHS
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'database'


class Config:
    CONFIG_TYPE = None
    # Secrets
    PERMANENT_SESSION_LIFETIME = timedelta(days=30)
    SECRET_KEY = 'REPLACE_WITH_YOUR_SECRET_KEY'
    ITEMS_COUNT_PER_PAGE = 10

    CATEGORY_SLUGS = {'shop': 'shop'}


class ProductionConfig(Config):
    DEBUG = False
    MYSQL_USERNAME = 'username'
    MYSQL_PASSWORD = 'password'
    MYSQL_DBNAME = DB_NAME
    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost/{}'.format(MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, '{}.db'.format(DB_NAME))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
