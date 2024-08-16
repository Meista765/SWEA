import sys; sys.stdin = open('D1/input_16240.txt')
T = int(input())

for tc in range(1, T+1):
    A = [[0] * 10 for _ in range(10)]
    
    pos_r, pos_c, N = map(int, input().split())
    
    start = pos_c
    end = pos_c + N-1
    for dr in range(N):
        A[pos_r + dr][start] = A[pos_r + dr][end] = 1
        
        if dr < N // 2:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1
        if start > end:
            start, end = end, start
    
    print(f'#{tc}')
    for row in A:
        print(*row)