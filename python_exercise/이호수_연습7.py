# # 061

# price = ['20180728', 100, 130, 140, 150, 160, 170]

# print(price[1:])

# # 062

# nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[::2])

# # 063

# nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[1::2])

# # 064

# nums = [1,2,3,4,5]
# print(nums[-1::-1])

# # 065

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0],interest[2])

# # 066

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# result = ' '.join(interest) # "문자열".join(리스트) 
# print(result)

# # 067

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# result = '/'.join(interest)
# print(result)

# # 068

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

# for i in interest:
#     print(i)

# print('\n'.join(interest))

# # 069

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# # 070

# data = [2,4,3,1,5,10,9]
# data.sort() # 오름차순 정리
# print(data)

# data2 = sorted(data)
# print(data2)

# # 071

# my_variable = ()
# print(type(my_variable))

# # 072

# my_variable = ("닥터 스트레인지","스플릿","럭키")

# # 073

# my_tuple = (1,)

# # 074

t = (1,2,3)
t[0] = 'a'