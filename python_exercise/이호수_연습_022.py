# # 211

# def function(str):
#     print(str)

# function("안녕")
# function("Hi")]

# # 212

# def 함수(a, b) :
#     print(a + b)

# 함수(3, 4)
# 함수(7, 8)

# # 213

# def 함수(문자열) :
#     print(문자열)
# 함수() # TypeError: 함수를 정의할 떄 정한 변수는 꼭 넣어야함

# # 214

# def 함수(a, b) :
#     print(a + b)

# 함수("안녕", 3) # TypeError : 문자열에 연산자 사용 안됨

# # 215

# def print_with_smile(userInput):
#     print(userInput+":D")

# # 216

# def print_with_smile(userInput):
#     print(userInput+":D")

# print_with_smile("안녕하세요")

# # 217

# def print_upper_price(userint):
#     print(userint*1.3)

# # 218

# def print_sum(num1,num2):
#     print(num1+num2)

# # 219

# def print_arthmetic_operation(num1,num2):
    
#     print("{} + {} = {}".format(num1,num2,num1+num2))
#     print("{} - {} = {}".format(num1,num2,num1-num2))
#     print("{} * {} = {}".format(num1,num2,num1*num2))
#     print("{} / {} = {}".format(num1,num2,num1/num2))

# 다른 방법

# def print_arithmetic_operation(a, b):
#     print(a, "+", b, "=", a + b)
#     print(a, "-", b, "=", a - b)
#     print(a, "*", b, "=", a * b)
#     print(a, "/", b, "=", a / b)

# # 220

# def print_max(num1, num2, num3):
#     if num1>=num2 and num1>=num3:
#         print(num1)
#     elif num2>=num1 and num2>=num3:
#         print(num2)
#     elif num3>=num2 and num3>=num1:
#         print(num3)

# 다른 방법

# def print_max(a, b, c) :
#     max_int = 0
#     if a > max_int :
#         max_int = a
#     if b > max_int :
#         max_int = b
#     if c > max_int :
#         max_int = c
#     print(max_int)