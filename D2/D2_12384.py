T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    # 최소값, 최대값 초기화
    min_val = float('inf')
    max_val = float('-inf')
    # index 순회하며 최대, 최소 갱신
    for i in range(N): # i: 1 ~ N-1
        # indexing 최소화를 위해 확인중인 수를 임시 변수에 저장
        tmp = A[i]
        
        # 최대값 갱신
        if max_val < tmp:
            max_val = tmp

        # 최소값 갱신
        if min_val > tmp:
            min_val = tmp

    print(f'#{tc} {max_val - min_val}')