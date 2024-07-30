T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    A = [0] * 5001 # idx: 0 ~ 5000
    for _ in range(N): # loop {N} times
        start, end = map(int, input().split())
        for i in range(start, end+1): # i: start ~ end
            A[i] += 1
    
    P = int(input())
    ans = ''
    for _ in range(P): # loop {P} times
        idx = int(input())
        ans = ' '.join([ans, str(A[idx])])
    
    print('#{}'.format(tc), end='')
    print(ans)