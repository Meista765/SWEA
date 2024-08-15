T = int(input())

for tc in range(1, T+1):
    N = 5
    A = [input() for _ in range(N)]
    
    max_len = 0
    for row in A:
        max_len = max(max_len, len(row))
    
    ans = ''
    for j in range(max_len):
        for i in range(N):
            try:
                ans += A[i][j]
            except:
                pass
    
    print(f'#{tc} {ans}')