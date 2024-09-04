import sys; sys.stdin = open('01953. 탈주범 검거/input.txt')
from collections import deque

# 파이프 형상; 화살표가 가리키는 방향이 열린 방향
delta = {
    1: [(-1, 0), (1,  0), (0, -1), (0, 1)],  # 1 : ↑, ↓, ←, →
    2: [(-1, 0), (1,  0)],                   # 2 : ↑, ↓
    3: [( 0, 1), (0, -1)],                   # 3 : ←, →
    4: [(-1, 0), (0,  1)],                   # 4 : ↑, →
    5: [( 1, 0), (0,  1)],                   # 5 : ↓, →
    6: [( 1, 0), (0, -1)],                   # 6 : ↓, ←
    7: [(-1, 0), (0, -1)],                   # 7 : ↑, ←
}

# 인접할 수 있는 파이프 형상
connectable_pipe_types = {
    1: {1, 2, 3, 4, 5, 6, 7},
    2: {1, 2, 4, 5, 6, 7},
    3: {1, 3, 4, 5, 6, 7},
    4: {1, 2, 3, 5, 6, 7},
    5: {1, 2, 3, 4, 6, 7},
    6: {1, 2, 3, 4, 5, 7},
    7: {1, 2, 3, 4, 5, 6}
}

def BFS():
    time_stamp = [[0] * len_c for _ in range(len_r)]
    
    queue = deque()
    queue.append((start_r, start_c))
    time_stamp[start_r][start_c] = 1
    
    while queue:
        cur_r, cur_c = queue.popleft()
        
        pipe_type = map_arr[cur_r][cur_c]
        connectables = connectable_pipe_types[pipe_type]
        for dr, dc in delta[pipe_type]:
            new_r = cur_r + dr
            new_c = cur_c + dc
            # 1. 새로운 인덱스가 범위를 벗어나지 않고,
            # 2. 해당 위치의 파이프가 현재 파이프와 연결되어 있어야 하며,
            # 3. 타임 스탬프에 시간이 찍히지 않은 위치여야 한다.
            if 0 <= new_r < len_r and 0 <= new_c < len_c and map_arr[new_r][new_c] in connectables and not time_stamp[new_r][new_c]:
                time_stamp[new_r][new_c] = time_stamp[cur_r][cur_c] + 1
                # 새로 찍은 타임스탬프가 최대 시간보다 작은 경우, 추가 탐색 진행
                if time_stamp[new_r][new_c] < limit:
                    queue.append((new_r, new_c))
    
    #디버그용
    for row in time_stamp:
        print(*row, sep='')
    
    result = 0
    for row in time_stamp:
        for time in row:
            if time > 0:
                result += 1
    
    return result


T = int(input())

for tc in range(1, T+1):
    len_r, len_c, start_r, start_c, limit = map(int, input().split())
    
    map_arr = [list(map(int, input().split())) for _ in range(len_r)]
    
    # 디버그용
    decode = {0: '.', 1: '┼', 2: '│', 3:'─', 4:'└', 5:'┌', 6:'┐', 7:'┘'}
    map_display = [[''] * len_c for _ in range(len_r)]
    for r in range(len_r):
        for c in range(len_c):
            map_display[r][c] = decode[map_arr[r][c]]
    for row in map_display:
        print(*row, sep='')
    
    print('#{} {}'.format(tc, BFS()))