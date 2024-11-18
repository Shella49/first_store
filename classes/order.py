class Order:
    '''
        Order - класс, представляющий заказ, с атрибутом
        products - список товаров в заказе
        Метод total_orders:
            метод класса который возвращает общее количество заказов
        Метод total_price:
            вычисляет общую стоимость всех товаров в заказе
    '''
    _total_order = 0
    _total_sum = 0
    
    def __init__(self, products):
        self.products = products     
        Order._total_order += 1
        Order._total_sum += self.total_price()
       
                   
    @classmethod
    def total_orders(cls):
        return cls._total_order
    @classmethod
    def total_orders_sum(cls):
        return cls._total_sum
    
    def total_price(self):
        return sum(product.price for product in self.products)
    
    def __str__(self):
        return f'(Total price = {self.total_price()})'