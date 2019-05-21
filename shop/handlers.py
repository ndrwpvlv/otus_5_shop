# -*- coding: utf-8 -*-

from flask import render_template
from flask.views import MethodView

from config import Config
from shop.models import Products


class Index(MethodView):
    """
    Index page class
    """

    def get(self):
        items = Products.query.order_by(-Products.id).limit(Config.ITEMS_COUNT_PER_PAGE).all()
        return render_template('index.html', items=items)


class Shop(MethodView):
    """
    Shop page class:
    If variable product_id exists return Product page
    Else return catalog
    """

    def get(self, product_id):
        return render_template('catalog.html', items=Products.query.order_by(-Products.id).limit(
            Config.ITEMS_COUNT_PER_PAGE).all()) if not product_id else \
            render_template('product.html', item=Products.query.filter_by(id=product_id).first())
