# # Quiz1

# class Test1:
#     def __init__(self):
#         self.hi="펭하~"
#         print(self.hi)

# # Quiz2

# class Test2:
#     def __init__(self):
#         self.name='펭수'
#         self.email="abc@naver.com"

# peng=Test2()
# print(peng.name)
# print(peng.email)

# # Quiz3

# class Test3:
#     def __init__(self):
#         self.name='펭수'
#         self.email="abc@naver.com"
    
#     def a(self):
#         print(self.name)
#         print(self.email)

# # Quiz4

# class Test4:
#     def __init__(self,name,phone,address):
#         self.name=name
#         self.phone=phone
#         self.address=address

# peng=Test4("펭수","010-1234-5678","남극")
# print(peng.name)
# print(peng.phone)
# print(peng.address)

# # Quiz5

# 나의 방법

# class Test5:
#     def __init__(self,dict):
#         self.dict=dict

# info={"name":"펭수",
#       'address':"남극",
#       'phone':"010-1234-5678"
#         }

# peng=Test5(info)
# print(peng.dict["name"])
# print(peng.dict["address"])
# print(peng.dict["phone"])

# 다른 방법

# class Test5:
#     def __init__(self,info):
#         self.name = info["name"]
#         self.address = info["address"]
#         self.phone = info["phone"]

# info = {
#     "name":"펭수",
#     "address":"남극",
#     "phone":"010-1234-5678"
#     }

# peng=Test5(info)

# print(peng.name)
# print(peng.address)
# print(peng.phone)


# # Quiz6

# class Test6:
#     def __init__(self):
#         pass

#     def calc1(self,num):
#         self.plus+=num
#         self.minus-=num

# # Quiz7

# class Test7:
#     def __init__(self):
#         pass

#     def calc2(self,num):
#         self.multiple*=num
#         self.divide/=num

# Test7=Test6()
