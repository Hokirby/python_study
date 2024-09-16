# import turtle
# turtle.shape("turtle")
# turtle.forward(100)
# turtle.mainloop()

# import turtle
# turtle.shape("circle")
# turtle.left(90)
# turtle.forward(100)
# turtle.mainloop()

# import turtle
# turtle.shape("circle")
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(120)
# turtle.forward(100)
# turtle.mainloop()

# a=int(input("정삼각형 한 변의 길이 : "))
# import turtle
# turtle.shape("circle")
# turtle.forward(a)
# turtle.left(120)
# turtle.forward(a)
# turtle.left(120)
# turtle.forward(a)
# turtle.mainloop()

# a=int(input("세로 길이: "))
# b=int(input("가로 길이 : "))
# import turtle
# turtle.shape("square")
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(a)
# turtle.left(90)
# turtle.forward(b)
# turtle.left(90)
# turtle.forward(a)
# turtle.mainloop()

# a=int(input("정육각형 한 변의 길이: "))
# import turtle
# turtle.shape("circle")
# for i in range(0,6):
#     turtle.left(60)
#     turtle.forward(a)
# turtle.mainloop()

# a=int(input("별의 한 변의 길이: "))
# import turtle
# turtle.shape("turtle")
# turtle.forward(a)
# turtle.left(144)
# turtle.forward(a)
# turtle.left(144)
# turtle.forward(a)
# turtle.left(144)
# turtle.forward(a)
# turtle.left(144)
# turtle.forward(a)
# turtle.mainloop()

# import turtle
# turtle.shape("triangle")
# for i in range(0,4):
#     turtle.forward(150)
#     turtle.left(144)
# turtle.forward(150)
# turtle.mainloop()

a=int(input("몇각형?: "))
b=int(input("한 변의 길이: "))
import turtle
turtle.shape("turtle")
for i in range(0,a):
    turtle.forward(b)
    turtle.left(360/a)
turtle.mainloop()


# from random import random
# print(random())

# from random import random
# print(random()*10)

# from random import random
# print("%d" %(random()*10))

# from random import random
# a=(random()*10)
# print("%d" %(a+1))

# for i in range(0,6):
#     from random import random
#     a=random()*44
#     print("%d" %(a+1))

# from random import randrange
# print(randrange(2,101,2))

# from random import randrange
# print(randrange(1,101,2))

# from random import randrange
# a=(randrange(0,101,1))
# b=int(input("수입력: "))
# if a>b:
#     print("UP")
# elif a<b:
#     print("DOWN")
# else:
#     print("GOOD")

# from random import randrange
# a=(randrange(0,101,1))
# while True:
#     b=int(input("수입력: "))
#     if a>b:
#         print("UP")
#     elif a<b:
#         print("DOWN")
#     else:
#         print("GOOD")
#         break

# from random import randrange
# a=(randrange(0,101,1))
# for i in range(3):
#     b=int(input("수입력: "))
#     if a>b:
#         print("UP")
#     elif a<b:
#         print("DOWN")
#     else:
#         print("GOOD")