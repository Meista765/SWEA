import sys; sys.stdin = open('D1/input_20397.txt', mode='r', encoding='UTF-8')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(M):
        pos_i, cnt = map(int, input().split())
        pos_i -= 1
        
        for di in range(1, cnt+1):
            left = pos_i - di
            right = pos_i + di
            if 0 <= left < N and 0 <= right < N and A[left] == A[right]:
                A[left], A[right] = 1 - A[left], 1 - A[right]
        
    print(f'#{tc}', *A)