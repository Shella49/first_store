class Customer:
    '''
    Customer - класс, представляющий клиента, с атрибутами:
    name -имя клиента
    orders - список заказов клиента
    '''
    def __init__(self,name,orders):
        self.name = name
        self.orders = orders # список заказов
        
    def __str__(self):
        return f"Client {self.name} make orders {self.orders}"
        
    