#Магазин
from classes.order import Order
from classes.customer import Customer
from classes.discount import Discount
from classes.product import Product

#Создаем продукты
product1 = Product("JVC", 1500)
product2 = Product("Samsung",2000)
product3 = Product("LG", 1200)
product4 = Product("Sony",5000)

#Создаем клиента
customer1 = Customer('Ivanov',orders=[])
customer2 = Customer('Maksimov',orders=[])
customer3 = Customer('Smirnova',orders=[])

#Создаем заказы
#orders1 = Order([product1, product2])
customer1.orders = Order([product1, product2])
#orders2 = Order([product2, product4])
customer2.orders = Order([product2, product4])
#orders3 = Order([product3, product1, product4])
customer3.orders = Order([product3, product1, product4])

#Общее количество заказов
print(f"Total orders: {Order.total_orders()}")
#Общая сумма всех заказов
print(f"Total sum of orders: {Order.total_orders_sum()}")

#Информация о клиентах и заказах
print(customer1)
print(customer2)
print(customer3)
