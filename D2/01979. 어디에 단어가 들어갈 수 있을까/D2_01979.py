import sys; sys.stdin = open('D2\input_01979.txt')

def solve():
    ans = 0
    
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                if i-1 < 0 or A[i-1][j] == 0:
                    pass
        
                if j-1 < 0 or A[i][j-1] == 0:
                    pass
    return ans

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {solve()}')