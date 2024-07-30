import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 건물 수(강물 포함)
    A = list(map(int, input().split())) # 높이 정보

    ans = 0
    for i in range(2, N-2):
        if A[i] == max(A[i-2:i+3]):
            ans += A[i] - max(A[i-2:i] + A[i+1:i+3])
    
    print(f'#{tc} {ans}')