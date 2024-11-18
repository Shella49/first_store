class Product:
    '''
    Класс Product, представляющий товар, с атрибутами 
    name - название товара,
    price - цена товара
    '''
    def __init__(self,name: str,price: float):
       self.name = name
       self.price = price

    def __str__(self):
       return f'Product: {self.name} price: {self.price}'