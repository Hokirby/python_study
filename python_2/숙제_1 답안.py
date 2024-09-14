
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


class Calc:
    def __init__(self,dict):
        self.dict=dict

    def calcRes(self,num1,num2,sign):
        global answer
        if (sign=="+"):
            answer=num1+num2
            self.result=answer
        elif (sign=="-"):
            answer=num1-num2
            self.result=answer
        elif (sign=="*"):
            answer=num1*num2
            self.result=answer
        elif (sign=="/"):
            answer=num1/num2
            self.result=answer

a=int(input("a 값을 입력해주세요 : "))
if a>=10:
    alist=[]
    for i in str(a):
        alist.append(i)
    a=int(alist[len(alist)-1])
b=int(input("b 값을 입력해주세요 : "))
if b>=10:
    blist=[]
    for i in str(b):
        blist.append(i)
    b=int(blist[len(blist)-1])
c=int(input("c 값을 입력해주세요 : "))
if c>=10:
    clist=[]
    for i in str(c):
        clist.append(i)
    c=int(clist[len(clist)-1])
d=int(input("d 값을 입력해주세요 : "))
if d>=10:
    dlist=[]
    for i in str(d):
        dlist.append(i)
    d=int(dlist[len(dlist)-1])
  
userInput={"a":a,
     "b":b,
     "c":c,
     "d":d  
}  

calculation=Calc(userInput)
print("값 :{}".format(calculation.dict))

while True:
    fstInput=input("첫번째 값을 입력해 주세요 : ")
    if fstInput=="a":
        fstInput=a
    elif fstInput=="b":
        fstInput=b
    elif fstInput=="c":
        fstInput=c
    elif fstInput=="d":
        fstInput=d
    sndInput=input("두번째 값을 입력해 주세요 : ")
    if sndInput=="a":
        sndInput=a
    elif sndInput=="b":
        sndInput=b
    elif sndInput=="c":
        sndInput=c
    elif sndInput=="d":
        sndInput=d
    sign=input("연산 기호를 입력해 주세요 : ")
    calculation.calcRes(fstInput,sndInput,sign)
    print(answer)
    if answer < 0 or answer >= 20:
        break