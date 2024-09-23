# # 251

# """
# class: 타입을 관련 데이터와 함수로 정의
# 객체: class로 만든 결과
# """

# # 252

# class Human:
#     pass

# # 253

# class Human():
#     pass

# areum = Human()

# # 254

# class Human():
#     def __init__(self):
#         print("응애응애")

# areum = Human()

# # 255

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         print("응애응애")


# areum = Human("아름", 25, "여자")
# print(areum.name)

# # 256

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

# areum = Human("조아름", 25, "여자")
# print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

# # 257

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

# areum = Human("조아름", 25, "여자")
# areum.who()

# # 258

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

#     def setinfo(self, nameSet, ageSet, sexSet):
#         self.name = nameSet
#         self.age = ageSet
#         self.sex = sexSet

# areum = Human("조아름", 25, "여자")
# areum.setinfo("이호수", 24, "여자")
# areum.who()

# # 259

# class Human():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
    
#     def __del__(self):
#         print("나의 죽음을 알리지 마라")    

#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

#     def setinfo(self, nameSet, ageSet, sexSet):
#         self.name = nameSet
#         self.age = ageSet
#         self.sex = sexSet
    
# areum = Human("조아름", 25, "여자")
# del(areum)

# # 260

# class OMG : 
#     def print() : # 생성자 self가 없음
#         print("Oh my god")

# myStock = OMG()
# myStock.print() # TypeError : myStock(self)이라는 값이 1개 주어졌지만 생성자 자리가 0개