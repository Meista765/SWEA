import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        min_idx = i
        for j in range(i+1, N):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

    print(f'#{tc}', *A)