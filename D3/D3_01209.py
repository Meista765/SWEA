import sys
sys.stdin = open('input.txt', 'r')

T = 10
N = 100
A = []

# 2차원 배열의 합을 구하는 함수
def sum_matrix() -> int:
    max_val = float('-inf')
    # 열과 행 방향 덧셈
    slash_sum = 0
    backslash_sum =0
    for i in range(N):
        # 합을 임시로 저장하는 변수 선언
        row_sum = 0
        col_sum = 0

        # 행, 열 합 계산
        for j in range(N):
            row_sum += A[i][j]
            col_sum += A[j][i]
        
        # 행, 열 최대합 갱신
        max_val = max(max_val, row_sum, col_sum)
        
        # 사선 방향 합 계산
        slash_sum += A[i][i]
        backslash_sum += A[i][-(i+1)]
    
    # 행, 열 최대합 갱신 후 사선 방향 최대합 갱신
    return max(max_val, slash_sum, backslash_sum)

for _ in range(T):
    tc = int(input())
    A = [list(map(int, input().split())) for _ in range(100)]
    
    print(f'#{tc}', sum_matrix())