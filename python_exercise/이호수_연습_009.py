# # 081

# a, b, *c = (0, 1 ,2, 3, 4, 5) # start expression
# print(a) # 0
# print(b) # 1
# print(c) # (2,3,4,5)

# # 082

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# valid_score = scores[:8]
# print(valid_scores)

# a, b, *valid_score = scores
# print(valid_score)

# # 083

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# valid_score = scores[1:9]
# print(valid_score)

# a, *valid_score, b = scores
# print(valid_score)

# # 084

# temp = {}

# # 085

# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(ice)

# # 086

# ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# ice["죠스바"] = 1200 # dict[key] = value / 추가
# ice["월드콘"] = 1500
# print(ice)

# # 087

# ice = {'메로나' : 1000,
#        '폴로포' : 1200,
#        '빵빠레' : 1800,
#        '죠스바' : 1200,
#        '월드콘' : 1500
#        }

# print("메로나 가격 : {}".format(ice['메로나']))

# # 088

# ice = {'메로나' : 1000,
#        '폴로포' : 1200,
#        '빵빠레' : 1800,
#        '죠스바' : 1200,
#        '월드콘' : 1500
#        }

# ice['메로나'] = 1300 # dict[key] = newValue / 변경

# # 089

# ice = {'메로나' : 1000,
#        '폴로포' : 1200,
#        '빵빠레' : 1800,
#        '죠스바' : 1200,
#        '월드콘' : 1500
#        }

# del ice['메로나'] # del dict[key] / key와 value 삭제
# print(ice)

# # 090

# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바'] # KeyError : 딕셔너리에 없는 키 사용
