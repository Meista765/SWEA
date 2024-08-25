import sys; sys.stdin = open('D3/01209. sum/input.txt')

for _ in range(10):
    tc = int(input())
    N = 100
    A = [[] for _ in range(N)]
    
    result = float('-inf')
    # 입력 및 행 최대
    for r in range(N):
        A[r] = list(map(int, input().split()))
        result = max(result, sum(A[r]))

    # 세로
    for c in range(N):
        tmp_sum = 0
        for r in range(N):
            tmp_sum += A[r][c]
        result = max(result, tmp_sum)
    
    # 대각
    sum_slash = 0
    sum_rslash = 0
    for d in range(N):
        sum_slash += A[d][d]
        sum_rslash += A[d][(N-1) - d]
    
    result = max(result, sum_slash, sum_rslash)
    
    print('#{} {}'.format(tc, result))