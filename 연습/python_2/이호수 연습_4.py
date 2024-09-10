# SyntaxError

# print("Syntax )

# NameError

# print(st)

# ZeroDivisionError

# print(10/0)

# IndexError

# lst = [1,2,3]
# print(lst[3])

# ValueError

# lst=[1,2,3]
# lst.remove(4)

# KeyError

# dic_a={"name":"펭수","age":"20"}
# print(dic_a[address])

# AttributeError

# import time
# time.sleepnow()

#FileNotFoundError

# f=open("test.txt","r")

# TypeError

# st="string"
# num=10
# print(st+num)

# try:
#     실행코드(에러발생가능)
# except:
#     실행코드(에러발생시)
# finally:
#     무조건 실행되어야하는 코드

# 예외 처리1

# try:
#     print(5/0)
# except:
#     print("ZeroDivision")

# try:
#     print("test")
# except:
#     print("ZeroDivision")

# 예외처리2

# try:
#     # print(5/0)
#     print("st)
# except ZeroDivisionError:
#     print("ZeroDivision")

# 예외처리 3

# try:
#     print(5/0)
#     # print("st)
# except ZeroDivisionError as e:
#     print(e)

# 에외처리 4

# try:
#     print(5/1)
# except:
#     print("Error")
# else:
#     print("No Error")


# 예외처리 5

# try:
#     print(5/1)
# except:
#     print("Error")
# finally:
#     print("END")

#예외처리 6 (여러 에러 처리하기)

# try:
#     # print(5/0)
#     print(st)
# except NameError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)

# 예외처리 7 (에러 무시하기)

# try:
#     # print(5/0)
#     print(st)
# except NameError as e:
#     pass
# except ZeroDivisionError as e:
#     print(e)

# print("testtesttest")

# 예외 처리 8 (오류 발생 시키기)

# try:
#     age=int(input("나이: "))
#     if age<0:
#         raise NotImplementedError
#     print("{}세".format(age))
# except NotImpelementedError:
#     print("음수값을 쓸 수 없습니다.")

# def div():
#     try:
#         a=int(input("첫번째 수 입력 : "))
#         b=int(input("두번쨰 수 입력: "))
#     except ValueError:
#         print("입력값이 숫자가 아닙니다.")
#         return
#     try:
#         c=a/b
#         print(c)
#     except ZeroDivisionError as e:
#         print(e)
    
# div()

# def birth():
#     try:
#         bd=int(input("태어난 년도는? "))
#     except ValueError:
#         print('태어난 년도가 숫자가 아닙니다.')
#         return
#     try:
#         age=2024-bd
#         if  bd>=0:
#             print("만 {}세".format(age))
#         elif bd<0:
#             raise ValueError
#     except ValueError:
#         print("태어난 년도가 음수값입니다.")

# birth()

# def rd(i):
#     try:
#         file=open(i,"r",encoding="UTF-8")
#         a=file.read()
#         return a
#     except FileNotFoundError as e:
#         return e
#     except PermissionError as f:
#         return f
#     except Exception as g:
#         return "Error: {}".format(g)
# i=input("파일명 입력: ")
# rdcontext=rd(i)
# print(rdcontext)

# rd()

# def readFile(filename):
#     try:

#         file = open(filename, "r")
#         context = file.read()
#         return context
    
#     except FileNotFoundError:
#         return "Error: 파일이 존재하지 않습니다."
    
#     except PermissionError:
#         return "Error: 파일에 접근 권한이 없습니다."
    
#     except Exception as e:
#         return "Error: {}".format(e)
    
# filename = input("파일명을 입력해주세요: ")
# filecontext = readFile(filename)
# print(filecontext)

# readFile()

# class a:
#     def init (self, b):
#         pass

# class c:
#     def str (self):
#         pass

# class e(class a):

# # 객체 지향 프로그래밍

# # timo

# # - 행동(속도)
# def timo_run():
#     speed=10

# # - 대사
# def timo_say():
#     print("티모 대위, 명을 받들겠습니다.")

# # - 스킬
# timo={"q":"실명다트","w":"신속한 이동","e":"맹독다트","r":"독버섯"}

# # lulu

# # - 행동(속도)
# def lulu_run():
#     speed=10

# # - 대사
# def lulu_say():
#     print("만나서 반갑습니다.")

# # 스킬
# lulu={"q":"글리터랜스","w":"변덕","e":"도와줘, 픽스","r":"급속한 성장"}

# # tristana

# # - 행동(속도)
# def tristana_run():
#     speed=10

# # - 대사
# def tristana_say():
#     print("일단 한번 쏘고 나면 또 쏘고 싶을 거에요!")

# # - 스킬
# tristana={"q":"신속한 홰자","w":"로켓 점프","e":"폭발물","r":"버스터 샷"}


# # 클래스

# # step1. 클래스 민들기
# class Character:
#     def run(self):
#         self.speed=10
    
#     def say(self):
#         print("티모 대위, 명을 받들겠습니다.")

# # step2. 객체 생성
# timo=Character()

# # step3. 속성 추가
# # timo={"q":"실명다트","w":"신속한 이동"."e":"맹독다트","r":"독버섯"}
# timo.q="실명다트"
# timo.w="신속한 이동"
# timo.e="멩독다트"
# timo.r="독버섯"

# # step4. 객체의 속성과 메소드 사용

# # 속성 4가지 출력
# print(timo.q)
# print(timo.w)
# print(timo.e)
# print(timo.r)

# # 메소드 2개 호출

# timo.run()
# timo.say()


# # 클래스2

# class Character:
#     def run(self):
#         self.speed=10
#     def say(self):
#         print("티모 대위, 명을 받들겠습니다.")
    
#     q="실명다트"
#     w="신속한 이동"
#     e="맹독다트"
#     r="독버섯"

# # 객체 생성
# timo=Character()

# # 속성 출력
# print(timo.q)
# print(timo.w)
# print(timo.e)
# print(timo.r)

# # 메소드 호출
# timo.say()

# # AttributeError
# # print(timo.speed)

# # Success
# timo.run()
# print(timo.speed)

# # lulu 객체 생성 및 속성 출력

# class Character:
#     def run(self):
#         self.speed=10
#     def say(self):
#         print("만나서 반갑습니다.")
#     q="글리터랜스"
#     w="변덕"
#     e="도와줘, 픽스"
#     r="급속한 성장"

# lulu=Character()

# print(lulu.q)
# print(lulu.w)
# print(lulu.e)
# print(lulu.r)

# lulu.say()
# lulu.run()
# print(lulu.speed)

# # tristana 객체 생성 및 속성 출력

# tristana=Character()

# print(tristana.q)
# print(tristana.w)
# print(tristana.e)
# print(tristana.r)

# # 클래스3

# class Character:
#     def __init__(self, speed, q,w,e,r):
#         self.speed=speed
#         self.q=q
#         self.w=w
#         self.e=e
#         self.r=r
#     def run(self):
#         self.speed=10

# timo=Character(0, "실명다트", "신속한 이동", "맹독다트"," 독버섯")

# print(timo.q)
# print(timo.w)
# print(timo.e)
# print(timo.r)

# # 이동 전
# # print(timo.speed)

# # 이동 후
# timo.run()
# print(timo.speed)

# # lulu 객체 생성 속성 출력

# class Character:
#     def __init__(self, speed, q,w,e,r):
#         self.speed=speed
#         self.q=q
#         self.w=w
#         self.e=e
#         self.r=r
#     def run(self):
#         self.speed=10

# lulu=Character(0,"글리터랜스","변덕","도와줘, 픽스","급속한 성장")

# print(lulu.q)
# print(lulu.w)
# print(lulu.e)
# print(lulu.r)

# lulu.run()
# print(lulu.speed)


# # tristana 객체 속성 출력

# tristana=Character(0,"신속한 화재","로켓 점프","폭발물","버스터샷")

# print(tristana.q)
# print(tristana.w)
# print(tristana.e)
# print(tristana.r)

# tristana.run()
# print(tristana.speed)

# # 클래스5

# class Character:
#     def __init__(self, speed, q,w,e,r):
#         self.speed=speed
#         self.q=q
#         self.w=w
#         self.e=e
#         self.r=r
#     def run(self):
#         self.speed=10
#     def __str__(self):
#         return "티모는 정찰대원입니다."

# timo=Character(0, "실명다트", "신속한 이동", "맹독다트"," 독버섯")

# # 객체 정보 출력
# print(timo)
# # <__main__.Character object at 0x000001EE9AFAB0B0>

# print(timo)
# # "티모는 정찰대원입니다."

# # 클래스6

# class Character:
#     def __init__(self, speed, q,w,e,r):
#         self.speed=speed
#         self.q=q
#         self.w=w
#         self.e=e
#         self.r=r
#     def run(self):
#         self.speed=10

# timo=Character(0, "실명다트", "신속한 이동", "맹독다트"," 독버섯")
# lulu=Character(0,"글리터랜스","변덕","도와줘, 픽스","급속한 성장")

# timo.run()
# lulu.run()

# print(timo.speed)
# print(lulu.speed)

# # 클래스7

# class A:
#     def momcar(self):
#         print("엄마차는 벤츠")
# class B(A):
#     def mycar(self):
#         print("내 차는 테슬라")

# b=B()
# b.momcar()
# b.mycar()