import sys; sys.stdin = open('D1/input_16244.txt')
T = int(input())

for tc in range(1, T+1):
    A = [[0] * 10 for _ in range(10)]
    
    pos_r, pos_c, N = map(int, input().split())
    
    for new_r in range(pos_r, pos_r + N):
        for new_c in range(pos_c, pos_c + N):
            if new_r == pos_r or new_r == pos_r + N-1 or new_c == pos_c or new_c == pos_c + N-1:
                A[new_r][new_c] = 1
    
    print(f'#{tc}')
    for row in A:
        print(*row)