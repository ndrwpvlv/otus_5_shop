# -*- coding: utf-8 -*-

from shop import db
from shop.models import Products


def make_db():
    db.drop_all()
    db.create_all()

def db_prepopulate():
    items = [
        ['Процессор AMD A6-9500E', 'images/amd-a6-9500e.png',
         'Частота 3ГГц, (Turbo 3.4ГГц), 2 ядра, Сокет AM4, OEM, AD9500AHM23AB, AD9500AHM23AB', 2200.0],
        ['Процессор AMD Ryzen Threadripper2990WX', 'images/amd-ryzen-tr-2990wx.png',
         'Частота 3ГГц, (Turbo 4.2ГГц), 32 ядер, L3 64МБ, Сокет sTR4, BOX, YD299XAZAFWOF', 127940.0],
        ['Процессор Intel Core i9-9960X', 'images/intel-core-i9-9960x.jpg',
         'Частота 3.1ГГц, (Turbo 4.4ГГц), 16 ядер, L3 22МБ, LGA2066, OEM, CD8067304126500', 128670.0],
        ['Процессор Intel Core i7-9700K', 'images/intel-core-i7-9700k.png',
         'Частота 3.6ГГц, (Turbo 4.9ГГц), 6 ядра, L3 12МБ, LGA1151v2, BOX, BX80684I79700K', 32990.0],
    ]

    for i in items:
        item = Products(*i)
        db.session.add(item)
        db.session.commit()

if __name__ == '__main__':
    make_db()
    db_prepopulate()
