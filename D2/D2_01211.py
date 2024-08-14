import sys
sys.stdin = open('input.txt', 'r')

N = 100

for _ in range(10):
    tc = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    ans = -1
    min_distance = float('inf')
    for column in range(N):  # column of A: 1 ~ N(100)
        i = 0
        j = column
        distance = 0
        if A[0][j] != 1:  # 첫 행의 요소가 1이 아니면 다음 탐색
            continue

        while i < N-1:  # loop until i reach N-1(99)
            i += 1  # go down
            distance += 1

            if (j+1 < N) and (A[i][j+1] == 1):
                while (j+1 < N) and (A[i][j+1] == 1):  # check weather "right" is available
                    j += 1
                    distance += 1
            elif (j-1 >= 0) and (A[i][j-1] == 1):
                while (j-1 >= 0) and (A[i][j-1] == 1):  # check weather "left" is available
                    j -= 1
                    distance += 1
        
        if distance <= min_distance:
            min_distance = distance
            ans = column
    
    print(f'#{tc} {ans}')