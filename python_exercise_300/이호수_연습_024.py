# # 231

# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result) # NameError : reseult 값이 정의 안됨

# # 232

# def make_url(userUrl):
#     print("www.{}.com".format(userUrl))

# make_url("naver")

# def make_url(userInput):
#     userUrl = "www." + userInput + ".com"
#     return userUrl

# print(make_url("naver"))

# # 233

# def make_list(userStr):
#     userList = []
#     for i in userStr:
#         userList.append(i)
#     return userList

# def make_list(userStr):
#     userList = list(userStr)
#     return userList

# print(make_list("abcd"))

# # 234

# def pickup_even(userList):
#     evenList = []
#     for i in userList:
#         if i % 2 ==0:
#             evenList.append(i)
#     return evenList

# print(pickup_even([3, 4, 5, 6, 7, 8]))

# # 235

# def convert_int(userStr):
#     strList = userStr.split(",")
#     intList = []
#     userInt = 0
#     for i in strList:
#         intList.append(int(i))
#     for k in range(len(intList)):
#         userInt += intList[k]*10**((2-k)*len(intList))
#     return userInt

# print(convert_int("1,234,567"))

# # 간단한 방법

# def convert_int (string) :
#     return int(string.replace(',', '')) # replace 함수

# print(convert_int("1,234,567"))

# # 236

# def 함수(num) :
#     return num + 4

# a = 함수(10) # a에 14 저장
# b = 함수(a)
# c = 함수(b)
# print(c)

# # 237

# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# # 238

# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)

# # 239

# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10)
# print(c)

# # 240

# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c) # 전역변수