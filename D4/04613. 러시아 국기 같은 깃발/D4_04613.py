import sys; sys.stdin = open('D4/input_04613.txt')

def solve():
    min_coloring = float('inf')
    
    for sec_a in range(1, N):
        for sec_b in range(sec_a + 1, N):
            tmp_coloring = 0
            
            # white
            for i in range(sec_a):
                for j in range(M):
                    if A[i][j] != 'W': tmp_coloring += 1
            
            # blue
            for i in range(sec_a, sec_b):
                for j in range(M):
                    if A[i][j] != 'B': tmp_coloring += 1
            
            # red
            for i in range(sec_b, N):
                for j in range(M):
                    if A[i][j] != 'R': tmp_coloring += 1
        
            min_coloring = min(min_coloring, tmp_coloring)
        
    return min_coloring

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    
    print(f'#{tc} {solve()}')