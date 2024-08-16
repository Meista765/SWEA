import sys; sys.stdin = open('D1/input_16242.txt')
T = int(input())

for tc in range(1, T+1):
    A = [[0] * 10 for _ in range(10)]
    
    pos_r, pos_c, len_c, len_r = map(int, input().split())
    
    cnt = 1
    for dr in range(len_r):
        if dr % 2 == 0:
            for dc in range(len_c):
                new_r = pos_r + dr
                new_c = pos_c + dc
                A[new_r][new_c] = cnt
                cnt += 1
        else:
            for dc in reversed(range(len_c)):
                new_r = pos_r + dr
                new_c = pos_c + dc
                A[new_r][new_c] = cnt
                cnt += 1
    
    print(f'#{tc}')
    for row in A:
        print(*row)