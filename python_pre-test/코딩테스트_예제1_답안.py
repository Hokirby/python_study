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


n = 5

# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]



matrix = [[0] * n for _ in range(n)]

direction = 0

row = 0
col = 0
number = 1


while True:
    if number == n**2 + 1:
        break

    matrix[row][col] = number
    nr = row + dx[direction]
    nc = col + dy[direction]


    if nr < 0 or nc < 0 or nr >= n or nc >= n or matrix[nr][nc] != 0: # 위치가 벗어남 or 0이 아닌 위치에 숫자를 넣으려 할 때
        direction = (direction + 1) % 4 # 그 즉시 방향 바꾸기

    row = row + dx[direction]
    col = col + dy[direction]

    number += 1


for mat in matrix:
    print(mat)
