# class Cat :
#     def __init__(self, name) :
#         if (name == "사자"):
#             self.type = "LION KING"
#         elif (name == "호랑이"):
#             self.type = "호랑이"

    
#     def animal(self):
#         print(self.type)



# # lion = Cat('사자')
# # lion.animal()

# from random import randrange
# # a=(randrange(0,101,1))
# # while True:
# #     b=int(input("수입력: "))
# #     if a>b:
# #         print("UP")
# #     elif a<b:
# #         print("DOWN")
# #     else:
# #         print("GOOD")
# #         break

# class Gatcha:
#     def __init__(self, answer):
#         self.answer = answer

#     def compare(self,num):
#         if self.answer>num:
#             print("UP")
#             return "UP"
#         elif self.answer<num:
#             print("DOWN")
#             return "DOWN"
#         else:
#             print("GOOD")
#             return "GOOD"

# randomNumber = Gatcha((randrange(0,101,1)))

# while True:
#     userInput = int(input("수입력: "))
#     check = randomNumber.compare(userInput)
#     if (check == "GOOD") :
#         break
