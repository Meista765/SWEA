import sys; sys.stdin = open('D3/input_01220.txt')

def solve():
    cnt = 0
    for j in range(N):
        flag = False
        for i in range(N):
            if A[i][j] == 1:
                flag = True
            
            if flag == True and A[i][j] == 2:
                cnt += 1
                flag = False
        
    return cnt

T = 10
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {solve()}')