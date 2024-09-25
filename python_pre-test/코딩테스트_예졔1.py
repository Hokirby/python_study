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

# n = 5

# # 우 하 좌 상
dx = [0,1,0,-1] # inList index 
dy = [1,0,-1,0] # outList index


# matrix = [[0] * n for _ in range(n)] # *를 붙이면 []없이 출력 

def booleanMake(row, col): # 조건을 간단히, while True문 사용하기 위해 함수 만들기
    if (row >= 0 and row < N and col >= 0 and col < N):
        return True
    else:
        return False


T = int(input("")) # 테스트 횟수

for testcase in range(1, T+1):
    N = int(input("정사각형 한 변의 길이: "))
    snail = [[0] * N for _ in range(N)]
    
    x, y = 0, -1
    direction = 0 # 0:right, 1:down, 2:left, 3 :up

    i = 1
    while (i <= (N**2)):
        x += dx[direction]
        y += dy[direction]

       
        while (booleanMake(x, y) and snail[x][y] == 0):
            snail[x][y]= i
            x += dx[direction]
            y += dy[direction]
            i += 1
        
        x -= dx[direction] # 범위 벗어남 : 돌아가기
        y -= dy[direction]
        
        direction = (direction + 1) % 4 # direction의 범위는 우하좌상(4가지)
            
    print(f"#{testcase}")
    for row in snail:
        print(*row)