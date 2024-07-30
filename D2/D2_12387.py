T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # Padding to prevent IndexError
    A = [0] + list(map(int, input().split()))

    # 부분합 행렬 계산 (Padding)
    S = [0 for _ in range(N+1)]
    tmp_sum = 0
    for i in range(1, N+1): #
        tmp_sum += A[i]
        S[i] = tmp_sum

    # 최소값, 최대값 초기화
    min_val = float('inf')
    max_val = float('-inf')
    for i in range(M, N+1): # i: M ~ N
        # 부분합 계산
        sub_sum = S[i] - S[i-M]

        # 최대값 갱신
        if max_val < sub_sum:
            max_val = sub_sum

        # 최소값 갱신
        if min_val > sub_sum:
            min_val = sub_sum

    print(f'#{tc} {max_val - min_val}')