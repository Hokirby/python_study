# class Calc:
#     def __init__(self,dict):
#         self.dict=dict

#     def calcRes(self,num1,num2,sign):
#         global answer
#         if (sign=="+"):
#             answer=num1+num2
#             self.result=answer
#         elif (sign=="-"):
#             answer=num1-num2
#             self.result=answer
#         elif (sign=="*"):
#             answer=num1*num2
#             self.result=answer
#         elif (sign=="/"):
#             answer=num1/num2
#             self.result=answer

# a=int(input("a 값을 입력해주세요 : "))
# if a>=10:
#     alist=[]
#     for i in str(a):
#         alist.append(i)
#     a=alist[len(alist)-1]
# b=int(input("b 값을 입력해주세요 : "))
# if b>=10:
#     blist=[]
#     for i in str(b):
#         blist.append(i)
#     b=blist[len(blist)-1]
# c=int(input("c 값을 입력해주세요 : "))
# if c>=10:
#     clist=[]
#     for i in str(c):
#         clist.append(i)
#     c=clist[len(clist)-1]
# d=int(input("d 값을 입력해주세요 : "))
# if d>=10:
#     dlist=[]
#     for i in str(d):
#         dlist.append(i)
#     d=dlist[len(dlist)-1]
  
# userInput={"a":a,
#      "b":b,
#      "c":c,
#      "d":d  
# }  

# calculation=Calc(userInput)
# print("값 :{}".format(calculation.dict))

# while True:
#     fstInput=input("첫번째 값을 입력해 주세요 : ")
#     if fstInput=="a":
#         fstInput=a
#     elif fstInput=="b":
#         fstInput=b
#     elif fstInput=="c":
#         fstInput=c
#     elif fstInput=="d":
#         fstInput=d
#     sndInput=input("두번째 값을 입력해 주세요 : ")
#     if sndInput=="a":
#         sndInput=a
#     elif sndInput=="b":
#         sndInput=b
#     elif sndInput=="c":
#         sndInput=c
#     elif sndInput=="d":
#         sndInput=d
#     sign=input("연산 기호를 입력해 주세요 : ")
#     calculation.calcRes(fstInput,sndInput,sign)
#     print(answer)
#     if answer<0 or answer>=20:
#         break