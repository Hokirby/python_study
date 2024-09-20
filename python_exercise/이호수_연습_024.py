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

def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)