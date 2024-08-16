import sys; sys.stdin = open('D3/input_01873.txt')
'''
문자	의미
.	    평지(전차가 들어갈 수 있다.)
*	    벽돌로 만들어진 벽
#	    강철로 만들어진 벽
-	    물(전차는 들어갈 수 없다.)
^	    위쪽을 바라보는 전차(아래는 평지이다.)
v	    아래쪽을 바라보는 전차(아래는 평지이다.)
<	    왼쪽을 바라보는 전차(아래는 평지이다.)
>	    오른쪽을 바라보는 전차(아래는 평지이다.)

다음 표는 사용자가 넣을 수 있는 입력의 종류를 나타낸다.

문자	동작
U	    Up : 전차가 바라보는 방향을 위쪽으로 바꾸고, 한 칸 위의 칸이 평지라면 위 그 칸으로 이동한다.
D	    Down : 전차가 바라보는 방향을 아래쪽으로 바꾸고, 한 칸 아래의 칸이 평지라면 그 칸으로 이동한다.
L	    Left : 전차가 바라보는 방향을 왼쪽으로 바꾸고, 한 칸 왼쪽의 칸이 평지라면 그 칸으로 이동한다.
R	    Right : 전차가 바라보는 방향을 오른쪽으로 바꾸고, 한 칸 오른쪽의 칸이 평지라면 그 칸으로 이동한다.
S	    Shoot : 전차가 현재 바라보고 있는 방향으로 포탄을 발사한다.
'''

T = int(input())

def find_position():
    for r in range(len_r):
        for c in range(len_c):
            if field[r][c] in ['^', 'v', '<', '>']:
                return r, c

def shoot():
    global pos_r, pos_c
    shooting_direction = {
        '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)
    }
    # 탱크 방향 확인
    tank = field[pos_r][pos_c]
    
    # 발사 방향 설정
    dr, dc = shooting_direction[tank]
    new_r = pos_r + dr
    new_c = pos_c + dc
    while 0 <= new_r < len_r and 0 <= new_c < len_c:
        # 착탄지가 벽돌인 경우
        if field[new_r][new_c] == '*':
            field[new_r][new_c] = '.'
            break
        # 착탄지가 강철 벽인 경우
        elif field[new_r][new_c] == '#':
            break
        
        # 추가 진행
        new_r += dr
        new_c += dc

def move(cmd:str):
    global pos_r, pos_c
    moving_direction = {
        'U': (-1, 0, '^'), 'D': (1, 0, 'v'), 'L': (0, -1, '<'), 'R': (0, 1, '>')
    }
    
    # 이동 방향 설정
    dr, dc, tank = moving_direction[cmd]
    new_r = pos_r + dr
    new_c = pos_c + dc
    field[pos_r][pos_c] = tank
    if 0 <= new_r < len_r and 0 <= new_c < len_c:
        if field[new_r][new_c] == '.':
            field[new_r][new_c] = tank
            field[pos_r][pos_c] = '.'
            pos_r, pos_c = new_r, new_c

for tc in range(1, T+1):
    len_r, len_c = map(int, input().split())
    field = [list(input()) for _ in range(len_r)]
    
    pos_r, pos_c = find_position()
    
    len_cmd = int(input())
    cmd_lst = input()
    for cmd in cmd_lst:
        if cmd == 'S':
            shoot()
        else:
            move(cmd)
    
    print(f'#{tc}', end=' ')
    for row in field:
        print(*row, sep='')