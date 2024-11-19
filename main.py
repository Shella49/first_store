#Магазин
from classes.order import Order
from classes.customer import Customer
from classes.discount import Discount
from classes.product import Product
#Создаем скидки на товары
discount_ALL = Discount(5)
discount_15 = Discount(15)
#Создаем продукты
product1 = Product("JVC", 1500)
product2 = Product("Samsung",2000)
product3 = Product("LG", 1200)
product4 = Product("Sony",5000)

#Создаем клиента
customer1 = Customer('Ivanov',Order([product1, product2], [5]))
customer2 = Customer('Maksimov',Order([product4],[5]))
customer3 = Customer('Smirnova',Order([product3, product1, product4],[5, 15]))

#Общее количество заказов
print(f"Total orders: {Order.total_orders()}")
#Общая сумма всех заказов
print(f"Total sum of orders: {Order.total_orders_sum()}")

#Информация о клиентах и заказах
print(customer1)
print(customer2)
print(customer3)
