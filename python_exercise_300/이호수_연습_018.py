# # 171

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)): # 리스트의 길이 만큼 반복
#     print(price_list[i]) # 리스트의 인덱스 활용

# # 172

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print(i, price_list[i]) 

# # 173

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list)):
#     print(len((price_list)-1)-i, price_list[i]) # 리스트의 길이 - 1 = 리스트 내 정보 개수

# # 174

# price_list = [32100, 32150, 32000, 32500]

# for i in range(len(price_list[:1]),len(price_list)):
#     print((90+10*i), price_list[i]) 

# # 175

# my_list = ["가","나","다","라"]

# for i in range(len(my_list)-1):
#     print(my_list[i], my_list[i+1])

# # 176

# my_list = ["가", "나", "다", "라", "마"]

# for i in range(len(my_list)-2):
#     print(my_list[i], my_list[i+1], my_list[i+2])

# # 177

# my_list = ["가", "나", "다", "라"]

# for i in range(-1, (-len(my_list)),-1):
#     print(my_list[i], my_list[i-1])

# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list[i], my_list[i-1])

# # 178

# my_list = [100, 200, 400, 800]

# for i in range(len(my_list)-1):
#     print(abs(my_list[i]-my_list[i+1])) # abs(음수/양수값) = 값 

# # 179

# my_list = [100, 200, 400, 800, 1000, 1300]

# for i in range(len(my_list)-2):
#     print(abs((my_list[i]+my_list[i+1]+my_list[i+2])/3)) # 실수값도 가능

# # 180

# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []

# for i in range(len(low_prices)):
#     volatility.append(high_prices[i]-low_prices[i])

# print(volatility)