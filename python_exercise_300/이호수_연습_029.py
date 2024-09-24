# # 281

# class Car:
#     def __init__(self, wheel, price):
#         self.wheel = wheel
#         self.price = price

# mycar = Car(2, 1000)
# print(mycar.wheel)
# print(mycar.price)

# # 282

# class bycycle(Car):
#     pass

# # 283

# class Bicycle(Car):
#     def __init__(self, wheel, price):
#         self.wheel = wheel
#         self.price = price

# mybicycle = Bicycle(2, 100)
# print(mybicycle.price)

# # 284

# class Bicycle(Car):
#     def __init__(self, wheel, price, systemDrive):
#         self.wheel = wheel
#         self.price = price
#         self.systemDrive = systemDrive

# mybicycle = Bicycle(2, 100, "SHIMANO")
# print(mybicycle.systemDrive)

# # 285

# class Autocar(Car):
#     def __init__ (self, wheel, price):
#         self.wheel = wheel
#         self.price = price
    
#     def infoPrint(self):
#         print("바퀴수", self.wheel)
#         print("가격", self.price)

# mycar = Autocar(4, 10000)
# mycar.infoPrint()

# # 286

# class Car:
#     def __init__(self, wheel, price):
#         self.wheel = wheel
#         self.price = price
    
#     def infoPrint(self):
#         print("바퀴수", self.wheel)
#         print("가격", self.price)

# class Bicycle(Car):
#     def __init__(self, wheel, price, systemDrive):
#         self.wheel = wheel
#         self.price = price
#         self.systemDrive = systemDrive

# mybicycle = Bicycle(2, 100, "SHIMANO")
# mybicycle.infoPrint()

# # 287

# class Car:
#     def __init__(self, wheel, price):
#         self.wheel = wheel
#         self.price = price
    
#     def infoPrint(self):
#         print("바퀴수", self.wheel)
#         print("가격", self.price)

# class  Autocar(Car):
#     def __init__(self, wheel, price):
#         super().__init__(wheel, price)

# class Bicycle(Car):
#     def __init__(self, wheel, price, systemDrive):
#         super().__init__(wheel, price)
#         self.systemDrive = systemDrive
    
#     def infoPrint(self):
#         super().infoPrint()    
#         print("구동계", self.systemDrive)

# my = Bicycle(2, 100, "SHIMANO")
# my.infoPrint()

# # 288

# class Mother:
#   def call(self):
#     print("Mother's call")

# class Son(Mother):
#   def call(self):
#     print("Son's call")

# me = Son()
# me.call()

# # 289

# class Mother:
#   def __init__(self):
#     print("Mother Created")

# class Son(Mother):
#   def __init__(self):
#     print("Son Created")

# me = Son()

# # 290

# class Mother:
#   def __init__(self):
#     print("Mother Created")

# class Son(Mother):
#   def __init__(self):
#     print("Son Created")
#     super().__init__()

# me = Son()