T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in reversed(range(N)): # i: N-1 ~ 0
        for j in range(i): # j: 1 ~ i-1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


    print(f'#{tc}', end=' ')
    print(*A)