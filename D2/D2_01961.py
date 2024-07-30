import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 행렬의 크기 입력 
    N = int(input())
    
    # 행렬 입력
    mtx = [list(map(int, input().split())) for _ in range(N)]
    
    # 회전 행렬 초기화
    mtx_90 = [[0 for _ in range(N)] for _ in range(N)]
    mtx_180 = [[0 for _ in range(N)] for _ in range(N)]
    mtx_270 = [[0 for _ in range(N)] for _ in range(N)]
    
    # 90도 회전
    ii, jj = 0, 0
    for j in range(N):
        for i in reversed(range(N)):
            mtx_90[ii][jj] = mtx[i][j]
            jj += 1
        ii += 1
        jj = 0
    
    # 180도 회전
    ii, jj = 0, 0
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            mtx_180[ii][jj] = mtx[i][j]
            jj += 1
        ii += 1
        jj = 0
        
    # 270도 회전
    ii, jj = 0, 0
    for j in reversed(range(N)):
        for i in range(N):
            mtx_270[ii][jj] = mtx[i][j]
            jj += 1
        ii += 1
        jj = 0
    
    # 정답 출력
    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(mtx_90[i][j], end = '')
        print(' ', end = '')
            
        for j in range(N):
            print(mtx_180[i][j], end = '')
        print(' ', end = '')
            
        for j in range(N):
            print(mtx_270[i][j], end = '')
        print()