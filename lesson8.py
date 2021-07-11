# Моносостояние для всех экземпляров
'''
class Cat:
    breed = 'pers'
'''

class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr
