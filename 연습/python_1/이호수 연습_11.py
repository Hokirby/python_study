
#
# st1="첫 번쨰 for문"
# st2="두번째 for문"
# for st in range(3):
#     print("{}\n{}".format(st1,st2))
#     for st in range(1):
#         print("{}".format(st2))

# for i in range(3):
#     print("첫 번째 for문")
#     for h in range(2):
#         print("두번째 for문")

# n=0
# j=0
# j_list=[1,2]
# for i in range(3):
#     print("이중 for 문 (i : {}\t\tj: 0)".format(n))
#     for j in j_list:
#         print("이중 for 문 (i : {}\t\tj: {})".format(n,j))
#     n+=1
# 어이없을 무
# for i in range(3):
#     for j in range(3):
#         print("이중 for 문 (i: {}\t\tj: {})".format(i,j))

# for i in range(2,10):
#     for j in range(1,10):
#         print("{}X{}={}".format(i,j,(i*j)), end=" ")
#     print()

# for i in range(1,10):
#     for j in range(2,10):
#         print("{}X{}={}".format(j,i,(i*j)), end=(" "))
#     print()

# i=0
# while 0<=i<=5:
#     print(i)
#     i=i+1

# while True:
#     print("무한반복 like 뽤로뽤로뽤로미")

# while True:
#     print("ㅁㅎㅂㅂ")
#     break
#     print("2번째 출력은 나오나요?")
# print('휴~')

# while True:
#     i=int(input("10보다 작은 정수 입력:"))
#     if i<10:
#         print("입력하신 값은 10보다 작습니다.")
#         break
#     else:
#         print("말 좀 들어요,,")
#         continue
# print("반복 종료!")

# i=0
# while 0<=i<=4:
#     i=i+1
#     print(i)
# for i in range(5):
#     i=i+1
#     print(i)

# while True:
#     num=int(input("수를 입력하시오: "))
#     if num==0:
#         break
# print("반복 종료")