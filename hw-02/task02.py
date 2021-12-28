"""Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина бытовой электроники 
(не менее двух свойств и методов). Реализуйте двух наследников товара, например, классы телевизор и холодильник, 
которые должны будут иметь в дополнение к наследуемым хотя бы по одному собственному уникальному свойству и методу.
Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами. 
Рассчитайте среднюю цену всех созданных товаров, используя главный класс. Реализуйте корректное сравнение двух товаров между собой 
по их исключительному свойству, например, два объекта-телевизора будут считаться равными между собой, если у них одинаковая диагональ. 
Сравните несколько товаров между собой."""

import numpy as np

class Product:
    def __init__(self,brand_name,model_name,price,**etc) -> None:
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.etc = etc

    @property
    def get_price(self):
        return self.price

    def calculate_footprint(self):
        """Method calculates occupied area of product if possible"""
        try:
            area = self.etc['length']*self.etc['width']
        except KeyError:
            print('There no data about length or width for this product.')
            return 'NoData'

    def discount10perc(self):
        """Return 10% discounted price"""
        return self.price*.9

class TV(Product):
    def __init__(self, brand_name, model_name, price,diagonal: int, **etc) -> None:
        super().__init__(brand_name, model_name, price, **etc)
        self.diagonal = diagonal

    def __eq__(self, __o: object) -> bool:
        return self.diagonal==__o.diagonal and self.brand_name==__o.brand_name

    def set_preview_clip(self,path_to_clip:str):
        """In any TV shop we can see some videos on a screens. Method adds the clip for preview"""
        self.preview_clip = path_to_clip

class Refrigerator(Product):
    def __init__(self, brand_name, model_name, price,min_temperature, **etc) -> None:
        super().__init__(brand_name, model_name, price, **etc)
        self.min_temperature = min_temperature

    def __eq__(self, __o: object) -> bool:
        return self.brand_name==__o.brand_name and self.model_name == __o.model_name

    def trade_in_sale(self,old_refrigerator: object):
        """Method return new discounted price of refrigerator if client brought old one for trade-in"""
        if old_refrigerator.is_instance(Refrigerator):
            return self.price-(old_refrigerator.price*0.75)
        else:
            raise TypeError("Needs 'Refrigerator' object in trade_in_sale method")


refs = [Refrigerator('Atlant','XM-6021-031',21037,-18,width=60,length=63),
        Refrigerator('POZIS','RK FNF-172',25805,-24,width=60,length=64),
        Refrigerator('Atlant','MXM-2835-90',15830,-18),
        Refrigerator('Atlant','XM-6021-031',23580,-18,width=60,length=63)]

tvs = [TV('Samsung','UE-32T5300',23364,32,width=15.1,length=46.5),
        TV('Xiaomi','Mi TV P1 43',33390,43),
        TV('LG','32LM6380',24700,32,width=18,length=46.4),
        TV('Samsung','UE-32T5300',27640,32,width=15.1,length=46.5)]

products = refs+tvs
prices = [i.get_price for i in products]
print("Mean price of products:",np.mean(prices))
print("TV[0] and TV[1] are equal: ",tvs[0]==tvs[1])
print("TV[0] and TV[3] are equal: ",tvs[0]==tvs[3])