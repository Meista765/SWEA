import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    
    max_sum = float('-inf')
    for i in range(N):
        for j in range(N):
            tmp_sum = A[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    tmp_sum += A[ni][nj]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
    
    print(f'#{tc} {max_sum}')