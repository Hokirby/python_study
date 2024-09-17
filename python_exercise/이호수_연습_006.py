# # 051

# movie_rank=["닥터 스트레인지","스플릿","럭키"]

# # 052

# movie_rank.append('배트맨') # 문자열 추가/ 문자열과 달리 리스트는 수정 가능
# print(movie_rank)

# # 053

# movie_rank.insert(1, "슈퍼맨") # 인덱스(위치)와 문자열 입력하여 추가
# print(movie_rank)

# # 054

# movie_rank.remove("럭키")

# del movie_rank[3] # 인덱스 사용해 제거

# print(movie_rank)

# # 055

# movie_rank = movie_rank[0:2]
# print(movie_rank)

# # 056

# lang1 = ["C","C++","JAVA"]
# lang2 = ["Python","Go","C#"]
# langs = lang1 + lang2 # 리스트 합하기
# print(langs)

# # 057

# nums = [1,2,3,4,5,6,7]
# print("max: {}".format(max(nums)))
# print("min: {}".format(min(nums)))

# # 058

# nums = [1,2,3,4,5]

# Nums=0
# for i in nums:
#     Nums+=i
# print(Nums)

# print(sum(nums)) # 모든 값 더하는 메서드

# # 059

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

# num = 0
# for i in cook:
#     num+=1
# print(num)

# print(len(cook)) # 길이(개수)를 알려줌/문자열,리스트,튜플등에 이용가능

# # 060

# nums = [1,2,3,4,5]
# average = sum(nums)/len(nums)
# print(average)