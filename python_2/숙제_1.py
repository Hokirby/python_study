# ##### 숙제 1
# """
# 계산기 만들기
# 숫자 a, b, c, d 를 입력 받고
# 사칙연산 할 수 있는 계산기를 만들어 주세요.


# 1. 만약 10이상 값을 입력했으면 해당 값은 0으로 설정해주세요
#     ex) a = 10 --> a = 0

# 2. 두개의 값을 입력 후, 기호를 입력하면 해당 결과를 출력해주세요 (while문 사용)

# 3. 만약 값이 20이상 이거나 0 이하일 경우 while문을 종료해주세요
# 클래스 생성해서 풀어주세요!
# """

# # 나의 방법

# # class Calc:
# #     def __init__(self):
# #         pass

# #     def calcRes(self,num1,num2,sign):
# #         global answer
# #         if (sign=="+"):
# #             answer=num1+num2
# #             self.result=answer
# #         elif (sign=="-"):
# #             answer=num1-num2
# #             self.result=answer
# #         elif (sign=="X"):
# #             answer=num1*num2
# #             self.result=answer
# #         elif (sign=="%"):
# #             answer=num1/num2
# #             self.result=answer


# # calculation=Calc()

# # while True:
# #     a=int(input("값입력: "))
# #     if a>=10:
# #         a=a-10
# #     b=int(input("값입력: "))
# #     if b>=10:
# #          b=b-10 
# #     sign1=input("기호: ")
# #     calculation.calcRes(a,b,sign1)
# #     print(answer)
# #     if answer<=0 or answer>=20:
# #         break

# #     c=int(input("값입력: "))
# #     if c>=10:
# #             c=c-10
# #     sign2=input("기호: ")
# #     calculation.calcRes(answer,c,sign2)
# #     print(answer)
# #     if answer<=0 or answer>=20:
# #         break

# #     d=int(input("값입력: "))
# #     if d>=10:
# #             d=d-10        
# #     sign3=input("기호: ")
# #     calculation.calcRes(answer,d,sign3)
# #     print(answer)
# #     if answer<=0 or answer>=20:
# #          break

# 함수로 코드 간결하게 하기

class Calc:
    def __init__(self):
        self.userInput={}
        self.answer=0

    def calcRes(self,num1,num2,sign):
        # global answer
        if (sign=="+"):
            self.answer=num1+num2
        elif (sign=="-"):
            self.answer=num1-num2
        elif (sign=="*"):
            self.answer=num1*num2
        elif (sign=="/"):
            self.answer=num1/num2
    
    def calcLast(self, strInput, intInput):

        if intInput>=10:
            strInput_list=[]
            for i in str(intInput):
                strInput_list.append(i)
                lastInt=int(strInput_list[len(strInput_list)-1])
        else:
             lastInt=intInput
        
        if (strInput=="a"):
                self.userInput["a"]=lastInt
        elif (strInput=="b"):
                self.userInput["b"]=lastInt
        elif (strInput=="c"):
                self.userInput["c"]=lastInt
        elif (strInput=="d"):
                self.userInput["d"]=lastInt
    
    def calcMatch(self,calcInput):
        return self.userInput[calcInput]



calculation=Calc()

a=int(input("a 값을 입력해주세요 : "))
b=int(input("b 값을 입력해주세요 : "))
c=int(input("c 값을 입력해주세요 : "))
d=int(input("d 값을 입력해주세요 : "))


calculation.calcLast("a",a)
calculation.calcLast("b",b)
calculation.calcLast("c",c)
calculation.calcLast("d",d)
print(calculation.userInput)


while True:
    fstInput=input("첫번째 값을 입력해 주세요 : ")
    fstInput=calculation.calcMatch(fstInput)
    sndInput=input("두번째 값을 입력해 주세요 : ")
    sndInput=calculation.calcMatch(sndInput)
    sign=input("연산 기호를 입력해 주세요 : ")
    calculation.calcRes(fstInput,sndInput,sign)
    print(calculation.answer)
    if calculation.answer<0 or calculation.answer>=20:
        break