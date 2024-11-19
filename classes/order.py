class Order:
    '''
        Order - класс, представляющий заказ, с атрибутом
        products - список товаров в заказе
        Атрибут класса  _total_orders: счетчик созданных заказов
        Атрибут класса  _total_sum: сумма всех заказов    
        Метод total_price:
            вычисляет общую стоимость всех товаров в заказе
    '''
    _total_order = 0
    _total_sum = 0
    
    def __init__(self, products, discounts):
        self.products = products 
        self.discounts = discounts    
        Order._total_order += 1
        Order._total_sum += self.total_price()
                       
    @classmethod
    def total_orders(cls):
        return cls._total_order
    
    @classmethod
    def total_orders_sum(cls):
        return cls._total_sum
    
    @staticmethod
    def applay_discount(price,discount):
        return price*(1- discount/100)
    
    def total_price(self):
        sum = 0
        for product in self.products:  #for all products
            
            for discount in self.discounts:  #for all discounts
                sum += Order.applay_discount(product.price, discount)
                print(f'For {product.name} discount {discount}')
        return sum
    
    def __str__(self):
        return f'(Total price = {self.total_price()})'