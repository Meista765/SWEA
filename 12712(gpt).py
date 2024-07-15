import sys
sys.stdin = open('input.txt', 'r')

def calculate_sum(arr, i, j, M, mode):
    total = arr[i][j]
    for d in range(1, M):
        if mode == 'plus':
            total += (arr[i][j-d] + arr[i][j+d] + arr[i-d][j] + arr[i+d][j] if 0 <= i-d and i+d < N and 0 <= j-d and j+d < N else 0)
        elif mode == 'cross':
            total += (arr[i-d][j-d] + arr[i-d][j+d] + arr[i+d][j-d] + arr[i+d][j+d] if 0 <= i-d and i+d < N and 0 <= j-d and j+d < N else 0)
    return total

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0
    for i in range(N):
        for j in range(N):
            plus_sum = calculate_sum(arr, i, j, M, 'plus')
            cross_sum = calculate_sum(arr, i, j, M, 'cross')
            max_sum = max(max_sum, plus_sum, cross_sum)

    print(f'#{tc} {max_sum}')