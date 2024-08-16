import sys; sys.stdin = open('D1/input_16235.txt')
T = int(input())

for tc in range(1, T+1):
    A = [[0] * 10 for _ in range(10)]
    
    pos_r, pos_c, N = map(int, input().split())
    
    cnt = 1
    for new_r in range(pos_r, pos_r + N):
        for new_c in range(pos_c, pos_c + N):
            A[new_r][new_c] = cnt
            cnt += 1
        
    print(f'#{tc}')
    for row in A:
        print(*row)