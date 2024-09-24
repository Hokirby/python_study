# # 121

# userInput = input("영어 문자 한 개 입력 : ")

# if userInput.islower() == True:
#     print(userInput.upper())
# else:
#     print(userInput.lower())

# # 122

# userScore = int(input("score : "))

# if 100 >= userScore >= 81:
#     print("grade is A")
# elif 80 >= userScore >= 61:
#     print("grade is B")
# elif 60 >= userScore >= 41:
#     print("grade is C")
# elif 40 >= userScore >= 21:
#     print("grade is D")
# elif 20 >= userScore >= 0:
#     print("grade is E")
# else:
#     print("잘못입력하셨습니다.")

# # 123

# 나의 방법

# userInput = input("입력 : ") 
# inputSplit = userInput.split(" ")
# userMoney = int(inputSplit[0])
# userCurrency = inputSplit[1]

# if userCurrency == "달러":
#     print("{:f} 원" .format(userMoney*1167))
# elif userCurrency == "엔":
#     print("{:f} 원" .format(userMoney*1.096))
# elif userCurrency == "유로":
#     print("{:f} 원" .format(userMoney*1268))
# elif userCurrency == "위안":
#     print("{:f} 원" .format(userMoney*171))
# else:
#     print("잘못입력하셨습니다.")

# 다른 방법

# rate = {"달러" : 1167,
#         "엔" : 1.096,
#         "유로" : 1268,
#         "위안" : 171
# }

# userInput = input("입력 : ")
# money, currency = userInput.split(" ")
# result = int(money) * rate[currency]
# print("{:f} 원". format(result))

# # 124

# num1 = int(input("number1: "))
# num2 = int(input("number2: "))
# num3 = int(input("number3: "))

# if num1 >= num2 and num1 >= num3:
#     print(num1)
# elif num2 >= num1 and num2 >= num3:
#     print(num2)
# elif num3 >= num1 and num3 >= num2:
#     print(num3)

# # 125

# dict_phone = { "011" : "SKT",
#               "016" : "KT",
#               "019" : "LGU",
#               "010" : "알수없음"
# }

# userPhone = input("휴대전화 번호 입력: ")
# userNum = userPhone.split("-")
# userID = userNum[0]
# print("당신은 {} 사용자입니다.".format(dict_phone[userID]))

# 다른 방법

# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")

# # 126

# 나의 방법

# userNum = input("우편번호 : ")

# if userNum[:2] != "01":
#     print("잘못입력하셨습니다.")
# else:
#     if userNum[2] == "0" or userNum[2] == "1" or userNum[2] == "2":
#         print("강북구")
#     elif userNum[2] == "4" or userNum[2] == "5" or userNum[2] == "6":
#         print("도봉구")
#     elif userNum[2] == "6" or userNum[2] == "7" or userNum[2] == "8" or userNum[2] == "9":
#         print("노원구")

# 디른 방법

# userNum = input("우편번호 : ")
# addNum = userNum[:3]
# if addNum in ["010","011","012"]:
#     print("강북구")
# elif addNum in ["013","014","015","016"]:
#     print("도봉구")
# elif addNum in ["017","018","019"]:
#     print("노원구")
# else:
#     print("잘못입력하셨습니다.")

# # 127

# inputID = input("주민등록번호: ")
# lastID = inputID.split("-")[1]
# sexID = lastID[0]
# if sexID in ["1", "3"]:
#     print("남자")
# elif sexID in ["2","4"]:
#     print("여자")
# else:
#     print("잘못입력하셨습니다.")

# # 128

# inputID = input("주민등록번호: ")
# sndinputID = inputID.split("-")[1]

# if 0 <= int(sndinputID[1:3]) <= 8:
#     print("서울 입니다.")
# # elif 9 <= int(sndinputID[1:3]) <= 12:
# #    print("부산 입니다.")
# else:
#     print("서울이 아닙니다.")

# # 129

# inputID = input("주민등록번호: ")
# inputID = inputID.split("-")
# fstinputID, sndinputID = inputID
# IDsum = int(fstinputID[0])*2 + int(fstinputID[1])*3 + int(fstinputID[2])*4 + int(fstinputID[3])*5 + int(fstinputID[4])*6 + int(fstinputID[5])*7 + int(sndinputID[0])*8 + int(sndinputID[1])*9 + int(sndinputID[2])*2 + int(sndinputID[3])*3 + int(sndinputID[4])*4 + int(sndinputID[5])*5        
# lastNum = 11- (IDsum%11)

# if str(lastNum) != sndinputID[6]:
#     print("유효하지 않은 주민등록번호입니다.")
# elif str(lastNum) == sndinputID[6]:
#     print("유효한 주민등록번호입니다.")

# # 130

# import requests

# url = "https://api.bithumb.com/v1/ticker"

# headers = {"accept": "application/json"}

# response = requests.get(url, headers=headers)

# print(response.text)
