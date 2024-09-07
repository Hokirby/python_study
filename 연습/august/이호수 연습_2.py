# 문제2 (반복문+함수)

# a=int(input("시작 : "))
# b=int(input("끝 : "))

# def test2(a,b):
#     isum=0
#     for i in range(a, b+1):
#         isum+=i

#     print("합: {}".format(isum))

# test2(a,b)

# 문제 3 (반복문 + 함수 + 리턴)

# a=int(input("시작 : "))
# b=int(input("끝 : "))

# def test3(a,b):
#     isum=0
#     for i in range(a,b+1):
#         isum+=i
#     return ("합: {}".format(isum))
# print(test3(a,b))

# 문제 4

# 기본매개변수

# def test4(start=1, end=100, step=1):
#     isum=0
#     for i in range(start, end+1, step):
#         isum+=i
#     return isum
    
# print(test4())
# print(test4(1,10,1))

# 키워드 매개변수

# def test4(start, end, step):
#     isum=0
#     for i in range(start, end+1, step):
#         isum+=i
#     return isum
    
# print(test4(start=1,end=10,step=1))

# num=int(input("수 입력: "))

# 문재6

# def test6(num):
#     for i in range(1,num+1):
#         if num%i==0:
#             print("{}의 약수는 {}입니다.".format(num,i))
# test6(8)

# b=[]
# def test6(i):
#     for j in range(0, i+1):
#         j+=1
#         if i%j==0:
#             b.append(j)
#     return print("{}의 약수 : {}".format(i,b))
# test6(8)


# def test7(i):
#     a=[]
#     asw=0
#     for j in range(0,i+1):
#         j+=1
#         if i%j==0:
#             a.append(j)
#             asw=asw+1
#     return print("{}의 약수 개수: {}".format(i,asw))

# test7(8)

# def fac(i):
#     b=1
#     for j in range(1,i+1):
#         b*=j
#     print(b)

# fac(8)

# tuple1=(10,20,30)
# print(tuple1[0])
# print(tuple1[1])
# print(tuple1[2])

