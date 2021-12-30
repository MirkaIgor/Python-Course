"""Реализуйте класс товар, в который включите свойства и методы общие для любого товара из магазина бытовой электроники 
(не менее двух свойств и методов). Реализуйте двух наследников товара, например, классы телевизор и холодильник, 
которые должны будут иметь в дополнение к наследуемым хотя бы по одному собственному уникальному свойству и методу.
Пополните ассортимент своего виртуального магазина несколькими разными товарами с различными параметрами. 
Рассчитайте среднюю цену всех созданных товаров, используя главный класс. Реализуйте корректное сравнение двух товаров между собой 
по их исключительному свойству, например, два объекта-телевизора будут считаться равными между собой, если у них одинаковая диагональ. 
Сравните несколько товаров между собой."""

import numpy as np

class Product:
    """
    Class is parent for all products in a shop.

    ----------------------------
    Attributes:
        brand_name      str
        model_name      str
        price       int or float
        discounted_price    int or float
        etc     dict
    Methods:
        get_price
            Method returns price of Product (property)
        calculate_footprint()
            Method calculates occupied area(m^2) of product if possible. It needs to be length and width filled
            in Product.etc
        discount_price(discount_perc)
            Method takes discount percent and returns discounted price and sets discounted_price by simple discount
    """
    def __init__(self,brand_name,model_name,price,**etc) -> None:
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.discounted_price = None
        self.etc = etc

    @property
    def get_price(self):
        """Method returns price of Product"""
        return self.price

    def calculate_footprint(self):
        """Method calculates occupied area(m^2) of product if possible"""
        try:
            area = self.etc['length']*self.etc['width']/(100*100)
            self.etc['area']=area
            return area
        except KeyError:
            print('There no data about length or width for this product.')
            return 'NoData'

    def discount_price(self,discount_perc):
        """Return discounted price and sets discounted_price"""
        self.discounted_price = self.price*(1-discount_perc/100)
        return self.discounted_price

class TV(Product):
    """
    Class represents TV object

    Extends Product
    --------------------------
    Attributes:
        diagonal    int
            Diagonal of the TV in inches
    Methods:
        set_preview_clip(path_to_clip: str)
            In any TV shop we can see some videos on a screens. Method sets the clip for preview
    """
    def __init__(self, brand_name, model_name, price,diagonal: int, **etc) -> None:
        super().__init__(brand_name, model_name, price, **etc)
        self.diagonal = diagonal
        self.preview_clip = None

    def __eq__(self, __o: object) -> bool:
        return self.diagonal==__o.diagonal

    def set_preview_clip(self,path_to_clip:str):
        """In any TV shop we can see some videos on a screens. Method adds the clip for preview"""
        self.preview_clip = path_to_clip

class Refrigerator(Product):
    """
    Class represents refrigerator.

    Extends Product
    -----------------------------
    Attributes:
        min_temperature     any numeric
    Methods:
        trade_in_sale(old_refrigerator: Refrigerator)
            Sets discounted price if client bring old refrigerator for trade in. Discount for new one
            is 75% from nominal price of old one.
    """
    def __init__(self, brand_name, model_name, price,min_temperature, **etc) -> None:
        super().__init__(brand_name, model_name, price, **etc)
        self.min_temperature = min_temperature

    def __eq__(self, __o: object) -> bool:
        return self.model_name == __o.model_name

    def trade_in_sale(self,old_refrigerator: object):
        """Method return new discounted price of refrigerator if client brought old one for trade-in"""
        if isinstance(old_refrigerator,Refrigerator):
            self.discounted_price = self.price-(old_refrigerator.price*0.75)
            return self.discounted_price
        else:
            raise TypeError("Needs 'Refrigerator' object in trade_in_sale method")


rf1 = Refrigerator('Atlant','XM-6021-031',21037,-18,width=60,length=63)
rf2 = Refrigerator('Atlant','MXM-2835-90',15830,-18)
rf3 = Refrigerator('POZIS','RK FNF-172',25805,-24,width=60,length=64)
rf4 = Refrigerator('Atlant','XM-6021-031',23580,-18,width=60,length=63)
tv1 = TV('Samsung','UE-32T5300',23364,32,width=15.1,length=46.5)
tv2 = TV('Xiaomi','Mi TV P1 43',33390,43)
tv3 = TV('LG','32LM6380',24700,32,width=18,length=46.4)
tv4 = TV('Samsung','UE-32T5300',27640,32,width=15.1,length=46.5)

products = [rf1,rf2,rf3,rf4,tv1,tv2,tv3,tv4]
prices = [i.get_price for i in products]
print("Mean price of products:",np.mean(prices))
print("TV[0] and TV[1] are equal: ",tv1==tv2)
print("TV[0] and TV[3] are equal: ",tv1==tv4)
print("Occupied area of product rf3: ", rf3.calculate_footprint()," m^2")
print("New price for POZIS RK FNF-172 with trade-in discount is ",rf3.trade_in_sale(Refrigerator('Чайка','600',4000,-16)))
tv2.set_preview_clip("https://www.youtube.com/watch?v=RK1K2bCg4J8")
tv3.discount_price(20)
print("New price for LG 32LM6380 with simple discount 20% is ",tv3.discounted_price)

