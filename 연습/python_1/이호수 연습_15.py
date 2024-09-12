#a={"name":"이호수","address":"춘천", "Blood Type":"B"}
# a["age"]=25
# a["address"]="고양"
# del a["Blood Type"]
# print(a)

# a={"key":"value","singer":"에스파"}
# a.update({"dancer":"HoneyJ"})
# a.get("key")
# print(a.keys())
# #output: dict_keys(['key', 'singer', 'dancer'])
# a.values()
# a.items()
# print(a.clear())
# #output: None

# a={}
# while True:
#     a.update({input("키 : ") : input("값 : ")})
#     b=int(input("입력을 계속하시겠습니까?\n진행시 1, 종료시 2를 입력하세요"))
#     if b==2:
#         break
# print(a)

# a={"커피":7,"펜":3,"종이컵":9,"콜라":20,"사이다":9}
# b=input("물건의 이름을 입력하세요: ")
# c=(a.get(b))
# print("{}의 수량은 {}개입니다.".format(b,c))

# a={}
# b=int(input("등록할 책 개수: "))
# for i in range(b):
#     a.update({(i+1):input("제목 : ")})
# print(a)

# st1="Python String"
# print(st1.find("g"))
# print(st1.count("String"))
# st1.lower()
# st1.upper()

# st2=" Python String "
# st2.strip()
# print(st2)

# st3="Python String"
# st3.replace("Python","O")
# print(st3)