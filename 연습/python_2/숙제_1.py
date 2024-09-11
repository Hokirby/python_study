##### 숙제 1
"""
계산기 만들기
숫자 a, b, c, d 를 입력 받고
사칙연산 할 수 있는 계산기를 만들어 주세요.


1. 만약 10이상 값을 입력했으면 해당 값은 0으로 설정해주세요
    ex) a = 10 --> a = 0

2. 두개의 값을 입력 후, 기호를 입력하면 해당 결과를 출력해주세요 (while문 사용)

3. 만약 값이 20이상 이거나 0 이하일 경우 while문을 종료해주세요
클래스 생성해서 풀어주세요!
"""

# # 해결중..

# class Calc:
#     def __init__(self):
#         pass

#     def calcSum(self,num1,num2):
#         answer=num1+num2
#         return answer
    
#     def calcSub(self,num1,num2):
#         answer=num1-num2
#         return answer
    
#     def calcMul(self,num1,num2):
#         answer=num1*num2
#         return answer
    
#     def calcDiv(self,num1,num2):
#         answer=num1/num2
#         return answer


#     def calcRes(self,num1,num2,sign):
#         if (sign=="+"):
#             self.calcRes=self.calcSum(num1,num2)
#         elif (sign=="-"):
#             self.calcRest=self.calcSub(num1,num2)
#         elif (sign=="X"):
#             self.calcRes=self.calcMul(num1,num2)
#         elif (sign=="%"):
#             self.calcRes=self.calcDiv(num1,num2)

# calculation=Calc()
# result=0

# while True:
#     a=int(input("첫번째 값: "))
#     if a>=10:
#         a=a-10
#     b=int(input("두번째 값: "))
#     if b>=10:
#          b=b-10 
#     sign1=input("기호: ")
#     result=calculation.calcRes(a,b,sign1)
#     print(result)
#     if result<=0 or result>=20:
#         break

#     c=int(input("세번째 값 : "))
#     if c>=10:
#             c=c-10
#     sign2=input("기호: ")
#     result=calculation.calcRes(result,c,sign2)
#     print(result)
#     if result<=0 or result>=20:
#         break

#     d=int(input("네번째 값 : "))
#     if d>=10:
#             d=d-10        
#     sign3=input("기호: ")
#     result=calculation.calcRes(result,d,sign3)
#     print(result)
#     if result<=0 or result>=20:
#          break
