import sys; sys.stdin = open('D3/input_04615.txt')

T = int(input())

def solve(cmd:list) -> tuple:
    delta = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    
    colors = [2, 2]  # colors[0] = black, colors[1] = white
    for idx in range(M):
        pos_x, pos_y, color = cmd[idx]
        
        # index 보정
        pos_x -= 1
        pos_y -= 1
        
        # 첫 자리 색칠
        A[pos_x][pos_y] = color
        # 돌을 놓고 개수 추가
        colors[color - 1] += 1
        
        for dx, dy in delta:
            found = False
            max_step = 0
            for step in range(1, N):
                new_x = pos_x + dx * step
                new_y = pos_y + dy * step
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or A[new_x][new_y] == 0:
                    break
                
                if A[new_x][new_y] == color:  # 자신과 같은 색상을 발견했다면,
                    found = True
                    max_step = step
                    break
            
            if found:
                for step in range(1, max_step):
                    new_x = pos_x + dx * step
                    new_y = pos_y + dy * step
                    
                    # 색칠
                    A[new_x][new_y] = color
                    
                    # 개수 변경
                        # color가 1(흑돌)이면, colors[0]++, colors[1]--
                        # color가 2(백돌)이면, colors[1]++, colors[0]--
                    colors[(color - 1) % 2]  += 1
                    colors[color % 2]  -= 1
    
    return colors

for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # 오셀로 판 초기화
    A = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N//2 - 1, N//2 + 1):
        for j in range(N//2 - 1, N//2 + 1):
            if (i + j) % 2 == 1:
                A[i][j] = 1
            else:
                A[i][j] = 2

    cmd = [list(map(int, input().split())) for _ in range(M)]
    
    print(f'#{tc}', *solve(cmd))