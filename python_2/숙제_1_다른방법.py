##### 숙제 1
"""
계산기 만들기
숫자 a, b, c, d 를 입력 받고
사칙연산 할 수 있는 계산기를 만들어 주세요.


1. 만약 10이상 값을 입력했으면 해당 값은 0으로 설정해주세요
    ex) a = 10 --> a = 0

2. 두개의 값을 입력 후, 기호를 입력하면 해당 결과를 출력해주세요 (while문 사용)

3. 만약 값이 20이상 이거나 0 이하일 경우 while문을 종료해주세요

"""

class Calc:
    def __init__(self):
        self.numbers = {}
    
    def isOverTen(self,num):
        if (num >= 10):
            return 0
        return num
    
    def saveNumbers(self, numbers):
        self.numbers = numbers

    def calculate(self,num1,num2,op):
        if (op == "+"):
            return self.numbers[num1] + self.numbers[num2]
        if (op == "-"):
            return self.numbers[num1] - self.numbers[num2]
        if (op == "*"):
            return self.numbers[num1] * self.numbers[num2]
        if (op == "/"):
            return self.numbers[num1] / self.numbers[num2]





calc = Calc()
numbers = {}
keys = ["a","b","c","d"]


for i in keys:
    num = int(input(f"{i} 값을 입력해 주세요 : "))
    numbers[i] = calc.isOverTen(num)

calc.saveNumbers(numbers)
print(f"값 : {numbers}")


while True:
    num1 = input("첫번째 값을 입력해 주세요 : ")
    num2 = input("두번째 값을 입력해 주세요 : ")
    op = input("연산 기호를 입력해 주세요 : ")

    rlt = calc.calculate(num1,num2,op)
    print(f"결과 값 : {rlt}")
    
    if (rlt >= 20 or rlt < 0):
        break