# # 221

# def print_reverse(str):
#     for i in str[-1::-1]:
#        print(i, end="")

# def print_reverse(str) :
#     print(str[::-1])

# print_reverse("python")

# # 222

# def print_score(list):
#     isum = 0
#     for i in list:
#         isum += i
#     print(isum/len(list))

# print_score ([1, 2, 3])

# # 223

# def print_even(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i)

# print_even ([1, 3, 2, 10, 12, 11, 15])

# # 224

# def print_keys(dict):
#     keys = dict.keys()
#     for i in keys:
#         print(i)

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# # 225

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}

# def print_value_by_key(dict, key):
#     print(dict[key])

# print_value_by_key  (my_dict, "10/26")

# # 226

# def print_5xn(str):
#     num = 0
#     for j in str:
#         num +=1
#         print(j, end="")
#         if num %5 == 0:
#             print()

# print_5xn("아이엠어보이유알어걸")

# # 227

# def print_mxn(userStr, userInt):
#     num = 0
#     for j in userStr:
#         num +=1
#         print(j, end="")
#         if num % userInt== 0:
#             print()

# print_mxn("아이엠어보이유알어걸", 3)

# # 228

# def calc_monthly_salary(annual_salary):
#     print(int(annual_salary/12))

# return 값 설정

# def calc_monthly_salary(annual_pay) :
#     monthly_pay = int(annual_pay / 12)
#     return monthly_pay

# calc_monthly_salary(12000000)

# # 229

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200) # = 으로 바인딩 처리

# # 터미널
# # 왼쪽: 100
# # 오른쪽: 200

# # 230

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200) # 같은 변수라면 위치 상관없다.