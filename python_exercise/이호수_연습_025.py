# # 241

# import datetime

# now = datetime.datetime.now()
# print(now)


# # 242

# import datetime

# print(type(datetime.datetime.now()))

# # 243

# import datetime

# now = datetime.datetime.today()

# for i in range(5,0,-1):
#     daysBf = datetime.timedelta(days=i)
#     date = now - daysBf
#     print(date)

# # 244

# import datetime

# now = now = datetime.datetime.today()

# print(now.strftime("%H:%M:%S"))

# # 245

# import datetime

# now = now = datetime.datetime.today()

# timeResult = datetime.datetime.strptime("2020-05-04", "%Y-%m-%d")

# print(timeResult, type(timeResult))

# # 246

# import time

# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# # 247

# import os # os.rename()
# from os import rename # rename()
# from os import * # getcwd(), rename(), ...
# import os as myos # myos.detcwd()


# # 248

# import os
# path = os.getcwd()
# print(path, type(path))

# # 249

# import os

# os.rename("C:/Users/admin/Desktop/python_study/python_exercise/test.txt",
#           "C:/Users/admin/Desktop/python_study/python_exercise/rename.txt"
#           )

# # 250

# import numpy

# for i in numpy.arange(0,5,0.1):
#     print(i)