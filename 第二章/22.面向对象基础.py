# class Car:
#     def __init__(self,c_color,c_brand,c_name,c_price):
#         #self:表示当前创建出来的实例对象
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car初始完毕")
#
# c1 = Car("red","BMW","X5",50000)
#
#
# print(c1.color)
# print(c1.__dict__)

class Car:
    #类属性,所以实例对象共享
    wheel = 4
    tax_rate = 0.1

    def __init__(self,c_color,c_brand,c_name,c_price):
        #self:表示当前创建出来的实例对象
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2
        print("Car初始完毕")
    def running(self):
        print(f"{self.brand}{self.name}列车开往那春天")

    def total_price(self,discount,rate):
        total_price = discount * self.price+rate * self.price
        return total_price

    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"

    def __eq__(self, other):
        return self.color==other.color and self.brand==other.brand and self.name==other.name and self.price==other.price

    def __lt__(self, other):
        return self.price<other.price
c1 = Car("red","BMW","X5",50000)
print(c1)
c2 = Car("red","BMW","X5",500000)
print(c2)
print(c1.wheel)
print(c1==c2)
print(c1>c2)
