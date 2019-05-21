# -*- coding: utf-8 -*-

from config import Config
from shop import app
from shop.handlers import Index, Shop


@app.context_processor
def inject_variables():
    return {'category_slugs': Config.CATEGORY_SLUGS}


""" URL RULES ADDING """

index = Index.as_view('index')
app.add_url_rule('/', view_func=index, methods=['GET', ])

shop = Shop.as_view('shop')
app.add_url_rule('/{}/'.format(Config.CATEGORY_SLUGS['shop']), view_func=shop, defaults={'product_id': None},
                 methods=['GET', ])
app.add_url_rule('/{}/<int:product_id>/'.format(Config.CATEGORY_SLUGS['shop']), view_func=shop, methods=['GET', ])
