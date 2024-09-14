# # 9월 7일  숙제

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
# 5. 룰루와 티모어택 합치기

# # 나의 방법

# class Champ:
#     def __init__(self, name):
#         self.name=name

#         if (name=="티모"):
#               self.health=500
#         elif (name=="룰루"):
#               self.health=300

#         self.timoskill={
#             "Q":["실명다트", "데미지: 30"],
#             "W":["신속한 이동", "데미지: 10"],
#             "E":["맹독다트", "데미지: 20"],
#             "R":["독버섯", "데미지: 50"],
#         }
#         self.luluskill={
#             "Q":["글리터랜스", "데미지: 30"],
#             "W":["변덕", "데미지: 10"],
#             "E":["도와줘, 픽스", "데미지: 20"],
#             "R":["급속한 성장", "데미지: 50"]
#         }

#     def skill(self,type):
#         if (self.name=="티모"):
#             print(self.timoskill[type])
#         elif (self.name=="룰루"):
#             print(self.luluskill[type])
    
# name=input("챔피언의 이름을 입력하시오. ")
# champion=Champ(name)
# print("체력: {}".format(champion.health))

# if name=="티모":
#         health=500
# elif name=="룰루":
#         health=300

# while True:
#     print("남은 체력: {}".format(health))
#     attack=input("챔피언을 공격할 스킬을 입력하세요. ")
    
#     if attack=="Q":
#             print(champion.skill(attack))
#             health=health-30
#     elif attack=="W":
#             print(champion.skill(attack))
#             health=health-10
#     elif attack=="E":
#             print(champion.skill(attack))
#             health=health-20
#     elif attack=="R":
#             print(champion.skill(attack))
#             health=health-50
#     else:
#         print("잘못된 스킬입니다.")
    
#     if 0>=health:
#           print("챔피언 처치")
#           break


# # 9월 9알 추가

# # while문 딕셔너리 인덱스 사용하기

# while True:
#     print("남은 체력: {}".format(health))
#     attack=input("챔피언을 공격할 스킬을 입력하세요. ")
    
#     if attack=="Q":
#             print(champion.skill(attack))
#             health-=champion.timoskill["Q"]["damage"]
#     elif attack=="W":
#             print(champion.skill(attack))
#             health-=champion.timoskill["W"]["damage"]
#     elif attack=="E":
#             print(champion.skill(attack))
#             health-=champion.timoskill["E"]["damage"]
#     elif attack=="R":
#             print(champion.skill(attack))
#             health-=champion.timoskill["R"]["damage"]
#     else:
#         print("잘못된 스킬입니다.")
    
#     if 0>=health:
#           print("챔피언 처치")
#           break


# # 클래스 안에 함수로 넣기

# class Champ:
#     def __init__(self, name):
#         self.name=name

#         if (name=="티모"):
#               self.health=500
#         elif (name=="룰루"):
#               self.health=300

#         self.timoskill={
#             "Q":{"name":"실명다트",
#                  "damage": 30},
#             "W":{"name" : "신속한 이동",
#                   "damage" : 10},
#             "E":{"name":"맹독다트",
#                   "데미지": 20},
#             "R":{"name": "독버섯",
#                  "damage": 50}
#         }
#         self.luluskill={
#             "Q":{"name":"글리터랜스",
#                  "damage": 30},
#             "W":{"name" : "변덕",
#                   "damage" : 10},
#             "E":{"name":"도와줘, 픽스",
#                   "데미지": 20},
#             "R":{"name": "급속한 성장",
#                  "damage": 50}
#         }

#     def skill(self,type):
#         if (self.name=="티모"):
#             print(self.timoskill[type])
#         elif (self.name=="룰루"):
#             print(self.luluskill[type])
    
#     def timoattack(self):
#          while True:  
#            print("남은 체력 : {}".format(self.health))
#            skill=input("챔피언을 공격할 스킬을 입력하세요. ")
#            if (skill=="Q"):
#                print(self.timoskill["Q"]["name"])
#                self.health-=self.timoskill["Q"]["damage"]
#            elif (skill=="W"):
#                print(self.timoskill["W"]["name"])
#                self.health-=self.timoskill["W"]["damage"]
#            elif (skill=="E"):
#                print(self.timoskill["E"]["name"])
#                self.health-=self.timoskill["E"]["damage"]
#            elif (skill=="R"):
#                print(self.timoskill["R"]["name"])
#                self.health-=self.timoskill["R"]["damage"]
#            else:
#               print("잘못된 스킬입니다.")
#            if 0>=self.health:
#               print("챔피언 처치")
#               break



#     def luluattack(self):
#          while True:
#              print("남은 체력 : {}".format(self.health))
#              skill=input("챔피언을 공격할 스킬을 입력하세요. ")
#              if (skill=="Q"):
#                  print(self.luluskill["Q"]["name"])
#                  self.health-=self.luluskill["Q"]["damage"]
#              elif (skill=="W"):
#                  print(self.luluskill["W"]["name"])
#                  self.health-=self.luluskill["W"]["damage"]
#              elif (skill=="E"):
#                  print(self.luluskill["E"]["name"])
#                  self.health-=self.luluskill["E"]["damage"]
#              elif (skill=="R"):
#                  print(self.luluskill["R"]["name"])
#                  self.health-=self.luluskill["R"]["damage"]
#              else:
#               print("잘못된 스킬입니다.")
#              if 0>=self.health:
#                print("챔피언 처치")
#                break
   
    
# name=input("챔피언의 이름을 입력하시오. ")
# champion=Champ(name)
# print("체력: {}".format(champion.health))

# if name=="티모":
#     champion.timoattack()
# elif name=="룰루":
#     champion.luluattack()


# if name=="티모":
#         health=500
# elif name=="룰루":
#         health=300


# # 9월 10일 다른 방법

# class Champ:
#     def __init__(self, name):
#         self.name = name     

#         if (name == "티모"):
#             self.hp = 500
#         else :
#             self.hp = 300
       
#         self.teemoSkill = {
#             "Q" : "실명 다트(Blinding Dart)",
#             "W" : "신속한 이동(Move Quick)",
#             "E" : "맹독 다트(Toxic Shot)",
#             "R" : "유독성 함정(Noxious Trap)"
#         }
#         self.luluSkill = {
#             "Q" : "반짝반짝 창(Glitterlance)",
#             "W" : "변덕쟁이(Whimsy)",
#             "E" : "도와줘, 픽스!(Help, Pix!)",
#             "R" : " 급성장(Wild Growth)"
#         }

#         self.damage = {
#             "Q" : 30,
#             "W" : 10,
#             "E" : 20,
#             "R" : 50
#         }


#     def skill(self, type):
#         if (self.name == "티모") :
#             print(self.teemoSkill[type])
#         else :
#             print(self.luluSkill[type])
        
#         self.damageToHp(type)
        
    
#     def damageToHp(self,type):
#         self.hp -= self.damage[type]
        
    



# name = input("챰피언 입력 : ")

# champ = Champ(name)


# while True:
#     skill = input('스킬을 입력해 주세요 : ')
#     champ.skill(skill)

#     if (champ.hp <= 0):
#         print("챔피언 처치")
#         break