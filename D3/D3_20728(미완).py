import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 총 주머니 수(N), 나눠줄 주머니(K)
    N, K = map(int, input().split())
    
    # 사탕
    arr = list(map(int, input().split()))
    
    # 크기 순으로 정렬
    sorted_arr = sorted(arr)
    
    # 정답 초기화
    min_diff = float('inf')
    
    # K개로 묶을 수 있는 인덱스까지 탐색
    for i in range(N - K + 1):
        tmp_diff = sorted_arr[i + K - 1] - sorted_arr[i]
        min_diff = min(min_diff, tmp_diff)

    print(f'#{tc} {min_diff}')