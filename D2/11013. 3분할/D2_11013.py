import sys; sys.stdin = open('D2\input_11013.txt')
T = int(input())

def solve():
    min_gap = float('inf')
    for i in range(1, N):
        for j in range(i+1, N):
            # print(A[:i], A[i:j], A[j:])
            partial_sum = [sum(A[:i]), sum(A[i:j]), sum(A[j:])]
            
            min_gap = min(min_gap, max(partial_sum) - min(partial_sum))
    
    return min_gap

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    
    result = solve()
    print(f'#{tc} {result}')