import sys; sys.stdin = open('D2/input_09490.txt')

def solve():
    max_gain = float('-inf')
    
    for i in range(N):
        for j in range(M):
            tmp_gain = A[i][j]
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                for k in range(1, A[i][j] + 1):
                    ni = i + di * k
                    nj = j + dj * k
                    if ni < 0 or ni >= N or nj < 0 or nj >= M:
                        break
                    tmp_gain += A[ni][nj]
            max_gain = max(max_gain, tmp_gain)
    
    return max_gain

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {solve()}')