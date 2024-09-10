# file = open("basic.txt", "w", encoding="UTF-8")
# file.write("펭하~")
# file.close()

# file=open("basic.txt","r",encoding="UTF-8")
# context=file.read()
# file.close
# print(context)

# file=open("quiz.txt","w",encoding="UTF-8")
# text1=input("입력1: ")
# file.write(text1)
# file.close()
# file=open("quiz.txt","r", encoding="UTF-8")
# context1=file.read()
# file.close()
# # print(context1)

# file=open("quiz1.txt","w",encoding="UTF-8")
# text2=input("입력2: ")
# file.write(text2)
# file.close()
# file=open("quiz1.txt","r",encoding="UTF-8")
# context2=file.read()
# file.close()
# print("{}\n{}".format(context1,context2))

# file=open("quiz2.txt","w",encoding="UTF=8")
# name=input("-당신의 이름은? ")
# age=input("-당신의 나이는? ")
# address=input("-당신의 주소는? ")
# file.write("{}\n{}\n{}".format(name, age, address))
# file.close()

# file=open("quiz2.txt","r",encoding="UTF-8")
# context=file.read()
# file.close()
# # print(context)

# file=open("quiz3.txt","w",encoding="UTF-8")
# file.write(context)
# file.close()

# file=open("quiz3.txt","r",encoding="UTF-8")
# context=file.read()
# file.close()
# print(context)

# file=open("quiz4.txt","w",encoding="UTF-8")
# email=input("-당신의 이메일 주소는? ")
# file.write("{}\n{}".format(context,email))
# file.close()
# file=open("quiz4.txt","r",encoding="UTF-8")
# context1=file.read()
# print(context1)

# file=open("quiz3.txt","r",encoding="UTF-8")
# text1=file.readline()
# text2=file.readline()
# text3=file.readline()
# text4=file.readline()
# print("{}{}{}{}".format(text1,text2,text3,text4))
# file.close()

# file=open("quiz3.txt","r",encoding="UTF-8")
# while True:
#     r=file.readline()
#     if r=="":
#         print("더이상 값이 존재하지 않습니다.")
#         file.close()
#         break
#     print(r)

# file=open("quiz3.txt","r",encoding="UTF-8")
# rr=file.readlines()
# print(rr)
# file.close()

# file=open("quiz3.txt",'r',encoding="UTF-8")
# r=file.readline()
# print(r)
# file.close()

# file=open("quiz3.txt","r",encoding="UTF-8")
# context=file.readlines()
# n=0
# for text in context:
#     print("{} : {}".format(n,text, end=""))
#     n+=1
# file.close

# file=open("quiz3.txt","w",encoding="UTF-8")
# print("---------------------")
# n=int(input("수정 번호 입력 : "))
# modify=input("수정값 입력 : ")
# print("---------------------")
# context[n]=modify+"\n"
# for c in context:
#     file.write(c)
#     print(c)
# file.close()
