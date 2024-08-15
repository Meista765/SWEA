import sys; sys.stdin = open('D3/input_11315.txt')

T = int(input())

def solve():
    # 좌하, 하, 우하, 우
    delta = [(1, -1), (1, 0), (1, 1), (0, 1)]
    
    for i in range(N):
        for j in range(N):
            for di, dj in delta:
                for k in range(5):  # k= 1 ~ 4
                    ni = i + di * k
                    nj = j + dj * k
                    if ni < 0 or ni >= N or nj < 0 or nj >= N or omok[ni][nj] != 'o':
                        break
                else:
                    return 'YES'
    
    return 'NO'

for tc in range(1, T+1):
    N = int(input())
    omok = [input() for _ in range(N)]
    
    print(f'#{tc} {solve()}')