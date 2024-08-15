import sys; sys.stdin = open('D2/input_11014.txt')

def solve():
    min_gap = float('inf')
    
    for i in range(1, N):
        for j in range(1, N):
            crop = [0, 0, 0]
            # 영역1 계산
            for l in range(i):
                for m in range(j):
                    crop[0] += A[l][m]
            
            # 영역2 계산
            for l in range(i, N):
                for m in range(j):
                    crop[1] += A[l][m]
            
            # 영역3 계산
            for l in range(N):
                for m in range(j, N):
                    crop[2] += A[l][m]

            min_gap = min(min_gap, max(crop) - min(crop))
    
    return min_gap

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {solve()}')