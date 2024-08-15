import sys; sys.stdin = open('D3\input_02805.txt')

def solve():
    crop = 0
    
    start = N //2
    end = start + 1
    for i in range(N):
        for j in range(start, end):
            crop += A[i][j]
        if i < N // 2:
            start, end = start - 1, end + 1
        else:
            start, end = start + 1, end - 1
    
    return crop

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]
    
    print(f'#{tc} {solve()}')