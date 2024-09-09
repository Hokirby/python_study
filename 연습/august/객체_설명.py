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

# timo = {"q":"실명다트", "w":"신속한 이동", "e":"맹독다트", "r":"독버섯"}
# lulu = {"q":"글리터랜스", "w":"변덕", "e":"도와줘, 픽스", "r":"급속한 성장"}


# # 나의 방법

# class Champ:
#     def __init__(self, name):
#         if (name=="티모"):
#             self.name="Timo"
#             self.q = "실명다트"
#             self.w = "신속한 이동"
#             self.e = "맹독다트"
#             self.r = "독버섯"
#         elif (name=="룰루"):
#             self.name="Lulu"
#             self.q = "글리터랜스"
#             self.w = "변덕"
#             self.e = "도와줘, 픽스"
#             self.r = "급속한 성장"


# UserInput=input("챔피언 이름을 입력하세요: ")
# character = Champ(UserInput)


# while True:
#     key=input("스킬 키를 입력하세요 : ")
#     if UserInput=="티모":
#         if key=="q":
#             print(character.q)
#         elif key=="w":
#             print(character.w)
#         elif key=="e":
#             print(character.e)
#         elif key=="r":
#             print(character.r)
#             break

# # while True:
# #     key=input("스킬 키를 입력하세요 : ")
# #     if UserInput=="룰루":
# #         if key=="q":
# #             print(character.q)
# #         elif key=="w":
# #             print(character.w)
# #         elif key=="e":
# #             print(character.e)
# #         elif key=="r":
# #             print(character.r)
# #         break

# # 다른 방법

# # 딕셔너리 사용
# # 변수명={"name":"호수","age":"24"}
# # 변수명["키"]="값"

# class Champ:
#     def __init__(self, name):
#         self.name=name
#         self.timoskill= {
#             "Q":"실명다트",
#             "W":"신속한 이동",
#             "E":"맹독다트",
#             "R":"독버섯"
#         }
#         self.luluskill={
#             "Q":"글리터랜스",
#             "W":"변덕",
#             "E":"도와줘, 픽스",
#             "R":"급속한 성장"
#         }
#     def skill(self,type):
#         if (self.name=="티모"):
#             print(self.timoskill[type])
#         elif (self.name=="룰루"):
#             print(self.luluskill[type])

# name=input("챔피언 입력: ")
# champion=Champ(name)

# while True:
#     skill=input("스킬을 입력해 주세요 : ")
#     champion.skill(skill)

#     if (skill=="R"):
#         break

# 추가
# 1. 티모의 체력은 500, 룰루의 체력은 300으로 설정
# 2. 스킬 입력시 전체 체력에서 스킬 데미지에 맞게 체력 깎기
# 3. Q:30, W:10, E:20, R:50
# 4. 체력이 이하가 되면 "챔피언 처치"가 나오면서 while문 break 

class Champ:
    def __init__(self, name):
        self.name=name

        if (name=="티모"):
              self.health=500
        elif (name=="룰루"):
              self.health=300

        self.timoskill={
            "Q":["실명다트", "데미지: 30"],
            "W":["신속한 이동", "데미지: 10"],
            "E":["맹독다트", "데미지: 20"],
            "R":["독버섯", "데미지: 50"],
        }
        self.luluskill={
            "Q":["글리터랜스", "데미지: 30"],
            "W":["변덕", "데미지: 10"],
            "E":["도와줘, 픽스", "데미지: 20"],
            "R":["급속한 성장", "데미지: 50"]
        }

    def skill(self,type):
        if (self.name=="티모"):
            print(self.timoskill[type])
        elif (self.name=="룰루"):
            print(self.luluskill[type])
    
name=input("챔피언의 이름을 입력하시오. ")
champion=Champ(name)
print("체력: {}".format(champion.health))

if name=="티모":
        health=500
elif name=="룰루":
        health=300

while True:
    print("남은 체력: {}".format(health))
    attack=input("챔피언을 공격할 스킬을 입력하세요. ")
    
    if attack=="Q":
            print(champion.skill(attack))
            health=health-30
    elif attack=="W":
            print(champion.skill(attack))
            health=health-10
    elif attack=="E":
            print(champion.skill(attack))
            health=health-20
    elif attack=="R":
            print(champion.skill(attack))
            health=health-50
    else:
        print("잘못된 스킬입니다.")
    
    if 0>=health:
          print("챔피언 처치")
          break
