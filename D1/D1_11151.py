T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    # 최대값
    max_val = 0
    for i in range(N-1): # i: 0 ~ N-2
        if max_val < A[i] + A[i+1]:
            max_val = A[i] + A[i+1]

    print(f'#{tc} {max_val}')