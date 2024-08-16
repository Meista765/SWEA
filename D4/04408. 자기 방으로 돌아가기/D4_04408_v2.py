import sys; sys.stdin = open('D4/input_04408.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    corridor = [0] * 401
    
    for _ in range(N):
        start, end = map(int, input().split())
        for i in range(start, end + 1):
            corridor[i] += 1
    
    print(f'#{tc} {max(corridor)}')