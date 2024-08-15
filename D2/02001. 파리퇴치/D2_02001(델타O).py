import sys; sys.stdin = open('D2\input_02001.txt')

def solve():
    max_gain = float('-inf')
    
    for i in range(N-M + 1):        # i= 1 ~ N-M
        for j in range(N-M + 1):    # j= 1 ~ N-M
            tmp_gain = 0
            for ni in range(i, i+M):
                for nj in range(j, j+M):
                    tmp_gain += A[ni][nj]
            max_gain = max(max_gain, tmp_gain)
    
    return max_gain

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {solve()}')