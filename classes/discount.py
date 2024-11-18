class Discount:
    ''' 
    Discount - класс для применения скидок, с атрибутами
    description - описание скидки
    discount_percent - поцент скидки
    '''
    def __init__(self,description: str,discount_percent: int):
        self.description = str
        self.discount_percent = discount_percent
        
    def __str__(self):
        return f'Dicount {self.description} is {self.discount_percent} percents'
        
    @staticmethod
    def discount(price,discount_percent):
        return price * (1 - discount_percent / 100)