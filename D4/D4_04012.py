import sys; sys.stdin = open('D4\input_04012.txt')

T = int(input())

def DFS(k, alst, blst):
    global ans
    if len(alst) > M or len(blst) > M:
        return
    
    if k == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M):
                for j in range(i+1, M):
                    asum += A[alst[i]][alst[j]] + A[alst[j]][alst[i]]
                    bsum += A[blst[i]][blst[j]] + A[blst[j]][blst[i]]
            ans = min(ans, abs(asum - bsum))
    
    DFS(k + 1, alst + [k], blst)
    DFS(k + 1, alst, blst + [k])
    

for tc in range(1, T+1):
    N = int(input())
    M = N // 2
    A = [list(map(int, input().split())) for _ in range(N)]
    
    ans = float('inf')
    DFS(0, [], [])
    
    print(f'#{tc} {ans}')