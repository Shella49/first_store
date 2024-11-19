class Discount:
    ''' 
    Discount - класс для применения скидок, с атрибутами
    description - описание скидки
    discount_percent - поцент скидки
    '''
    def __init__(self,discount_percent: int):
        self.discount_percent = discount_percent
        
    def __str__(self):
        return f'Dicount is {self.discount_percent} percents'
    
        