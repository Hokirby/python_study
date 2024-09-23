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

import datetime

now = now = datetime.datetime.today()

timeResult = datetime.datetime.strptime("2020-05-04", "%Y-%M-%D %H:%M:%S")

print(timeResult, type(timeResult))
