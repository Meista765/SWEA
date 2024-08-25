import sys; sys.stdin = open('D2/12387. 구간합/input_12387.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [0] + list(map(int, input().split()))
    
    # 0번 index는 dummy
    sub_sum = [0] * (N+1)
    
    # 구간합 생성
    tmp = 0
    for idx in range(1, N+1):
        tmp += A[idx]
        sub_sum[idx] = tmp
    
    # 최대, 최소 구간합 계산
    min_sum = float('inf')
    max_sum = float('-inf')
    for idx in range(M, N+1):
        tmp = sub_sum[idx] - sub_sum[idx-M]
        min_sum = min(min_sum, tmp)
        max_sum = max(max_sum, tmp)

    # 결과 출력
    print('#{} {}'.format(tc, max_sum - min_sum))