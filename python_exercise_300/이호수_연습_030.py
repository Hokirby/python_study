# # 291

# f = open("PurchaseItem.1.txt", mode = "wt", encoding = "UTF-8")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420")
# f.close()

# # 292

# f = open("PurchaseItem2.txt", mode ="wt", encoding = "UTF-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()

# # 293

# import csv

# f = open("PurchaseItem.csv", mode ="wt", encoding = "cp949", newline = '')
# writer = csv.writer(f)
# writer.writerow(["종목명","종목코드","PER"])
# writer.writerow(["삼성전자","005930",15.59])
# writer.writerow(["NAVER","035420",55.82])
# f.close()

# # 294

# f = open("PurchaseItem.1.txt", mode = "r", encoding = "UTF-8")
# lines = f.readlines()

# codes = []
# for line in lines:
#     code = line.strip() # '\n' 제거
#     codes.append(code)

# f.close()

# # 295

# f = open("PurchaseItem2.txt", mode = "r", encoding = "UTF-8")
# lines = f.readlines()

# items ={}

# for line in lines:
#     line = line.strip()
#     lineList = line.split(" ")
#     items[lineList[1]] = lineList[0]

# print(items)

# f.close()

# # 296

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)

# # 297

# per = ["10.31", "", "8.00"]
# rePER= []


# for i in per:
#     try:
#         float(i)
#     except:
#         i = 0
#     rePER.append(i)

# print(rePER)

# # 298

# try :
#     b = 3/0
# except ZeroDivisionError:
#     print(ZeroDivisionError)

# # 299

# data = [1, 2, 3]

# try:
#     for i in range(5):
#         print(data[i])

# except IndexError as I:
#     print(I, "인덱스 값이 초과했습니다.")

# # 300

# '''
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
# '''

# per = ["10.31", "", "8.00"]

# try:
#     for i in per:
#         print(float(i))

# except ValueError as V:
#     print(V)
#     i = 0
#     per.append(i)

# else:
#     print(f"리스트를 다음과 같이 초기화합니다.\n per: {per.clear()}")

# finally:
#     print(f"최종 PER: {per}")