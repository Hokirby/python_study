# def 함수 이름():
#     문장
# 1. 긴 코드를 축약할때

# def 인사():
#     print("안녕하세요")
#     print("반갑습니다")
#     print("또 만나요")

# # 호출
# 인사()
# 인사()
# 인사()

# 2. 마법의 모자를 만들고 싶을때

# def 함수 이름(매개변수,매개변수,...):
#   문장

# def 마법모자(구멍):
#     print(구멍+1)

# # 호출 # 인자
# 마법모자(1)
# 마법모자(2)
# 마법모자(3)

# 3. 긴코드 축약 + 마법모자를 만들고 싶을때

# def hi(name):
#     print("{}님 안녕하세요.".format(name))
#     print("{}님 반갑습니다.".format(name))
#     print("{}님 또 만나요.".format(name))

# # 호출
# hi("닝닝")
# hi("쇼타로")

# 예제 1

# def ex1(n):
#     for i in range(n):
#         print("안녕하세요")
#     print()

# ex1(1)
# ex1(2)
# ex1(3)

# 예제 2

# def ex2(n,s):
#     for i in range(n):
#         print(s)
#     print()

# ex2(1,"안녕하세요")
# ex2(3,"반갑습니다")
# ex2(5,"또 만나요")

# TypeError

# def TypeError(n,s):
#     for i in range(n):
#         print("{}회 > {}".format(i+1,s))

# TypeError(2,"Hi")
# # TypeError(3)
# # TypeError(3, "Hi","Bye")

# 리턴(return)

# a=input("data: ")
# print(a)

# def 함수 이름():
#   문장
#   return 자료

# # return 사용 O
# a=input("data: ")
# print(a)

# # return 사용 X

# b=print("8월03일")
# print(b)

# print() 사용

# def num1():
#     print(10)

# def num2():
#     print(20)

# print(num1()+num2())

# return

# def num3():
#     return 30

# def num4():
#     return 40

# print(num3()+num4())

# dict_a={1:"a",2:"b",3:"c"}
# print(dict_a.get(1))
# print(dict_a.get(2))
# print(dict_a.get(3))

# print(dict_a.clear())
# dict_a.clear()
# print(dict_a)

# 자료 없이 리턴
# def returnTest():
#     print("A위치 입니다.")
#     return

# returnTest()
# print(returnTest())

# 자료와 함께 리턴
# def returnTest():
#     print("A위치 입니다.")
#     return 100

# print(returnTest())

# 추가
# def returnTest():
#     print("A위치 입니다.")
#     return
#     print("B위치 입니다.")

# print(returnTest())

# def 함수 이름(매개변수):
#   변수=초기값
#   #문장
#   #문장
#   #문장
#   return 변수

# 문제1 (반복문)

# a=int(input("시작 : "))
# b=int(input("끝 : "))
# isum=0
# for i in range(a, b+1):
#     isum+=i
# print("합: {}".format(isum))

