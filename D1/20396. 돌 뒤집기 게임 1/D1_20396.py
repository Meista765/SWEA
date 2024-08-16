import sys; sys.stdin = open('D1/input_20396.txt', mode='r', encoding='UTF-8')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(M):
        pos_i, cnt = map(int, input().split())
        pos_i -= 1
        
        color = A[pos_i]
        
        for ni in range(pos_i + 1, pos_i + cnt):
            if 0 <= ni < N:
                A[ni] = color
        
    print(f'#{tc}', *A)