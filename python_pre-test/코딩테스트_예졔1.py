'''

달팽이 순회
n * n 정사각형이 있을때
해당 정사각형의 값을 1 부터 n**2 까지
달팽이 순회 해주세요

'''

# 정답 예시
'''
[1, 2, 3, 4, 5]
[16, 17, 18, 19, 6]
[15, 24, 25, 20, 7]
[14, 23, 22, 21, 8]
[13, 12, 11, 10, 9]
'''

1  2  3  
8  9  4
7  6  5

1   2   3  4
14  15  16 5
13  20  17 6
12  19  18 7
11  10  9  8



8, 121314, 141516

# n = 5

# # 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]



# matrix = [[0] * n for _ in range(n)]


n = int(input("정사각형 한 변의 길이: "))

outList = []
inList = []

# for j in range(n):
#     outList.append(inList)


while True:
    for i in range((n**2)):
      outList[int(i/n)].append(i+1)
      if x / n == 1 and x % n == 1 :
         x = n, y -= 1
      elif x 


# while True:

#     if : h / n == 1:
#         outList[0:n][n-1]= h

#     elif : h / n == 2 and h % n <= n - 2 :
#         outList[n-1][n-1::-1] = h
    
#     elif : n-2 <= h <=

for k in outList:
    print(k)

