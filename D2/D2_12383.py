import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    # 최대 낙폭
    max_diff = 0

    for i, now in enumerate(A): # i: 0 ~ N-1 / val <- A[i]
        # i+1 ~ N-1까지 본인보다 작은 블럭의 수를 저장
        cnt = 0
        for j in range(i+1, N): # j: i+1 ~ N-1
            # 현재 검토중인 수보다 작은 수만 카운트
            if A[j] < now:
                cnt += 1
        
        # 검토중인 낙폭이 최대 낙폭보다 크면 갱신
        if cnt > max_diff:
            max_diff = cnt
            
    print(f'#{tc} {max_diff}')