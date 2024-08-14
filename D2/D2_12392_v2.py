import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1): # tc: 1 ~ T
    N = int(input())
    A = list(map(int, input().split()))

    ans = f'#{tc} '
    
    for i in range(10): # i: 0 ~ N-1
        if i % 2 == 0: # 짝수
            max_idx = i
            for j in range(i, N):
                if A[j] > A[max_idx]:
                    max_idx = j
            A[i], A[max_idx] = A[max_idx], A[i]
        else: # 홀수
            min_idx = i
            for j in range(i, N):
                if A[j] < A[min_idx]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        
        ans += str(A[i]) + ' '

    print(ans)
