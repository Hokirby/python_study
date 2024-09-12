
# st="It is a fun python class"
# a=0
# s=0
# for i in st:
#    if  i=="a":
#     a=a+1
#    elif i=="s":
#     s=s+1
# print("알파벳 'a'의 개수: {}\n알파벳 's' 개수: {}".format(a,s))

# dsum=0
# ssum=0
# a=int(input("수를 입력하세요: "))
# for i in range(1,a+1):
#     if i%2==0:
#         dsum=dsum+i
#     else:
#         ssum=ssum+i
# print("총 짝수의 합: {}\n총 홀수의 합 : {}".format(dsum,ssum))

# tfsum=0
# for i in range(1, 101):
#     if i%3==0 and i%5==0:
#         tfsum=tfsum+i
# print("1~100사이의 값 중 3의 배수이며, 5의 배수에 해당하는 합: {}".format(tfsum))

# a=int(input("첫번째 수를 입력하세요: "))
# b=int(input("두번째 수를 입력하세요: "))
# absum=0
# basum=0
# if a>b:
#     for i in range(b,a+1):
#         absum=absum+i
#     print("두 수의 범위안의 합: {}".format(absum))
# elif a<b:
#     for i in range(a, b+1):
#         basum=basum+i
#     print("두 수의 범위의 합: {}".format(basum))
# else:
#     print("두 수는 같은 수 입니다.")