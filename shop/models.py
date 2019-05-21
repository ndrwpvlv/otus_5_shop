# -*- coding: utf-8 -*-

from shop import db


class Products(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(256), index=True)
    image_url = db.Column(db.String(256), index=True)
    caption = db.Column(db.Text)
    price = db.Column(db.Float)

    def __init__(self, title, image_url, caption, price):
        self.title = title
        self.image_url = image_url
        self.caption = caption
        self.price = price
