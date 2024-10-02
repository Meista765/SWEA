import sys

sys.stdin = open('D3/22683. 나무 베기/input.txt')
from collections import deque

U, R, D, L = range(4)

rotate_cnt = [
    [0, 1, 2, 1],
    [1, 0, 1, 2],
    [2, 1, 0, 1],
    [1, 2, 1, 0],
]

class Car:
    def __init__(self, row:int=None, col:int=None, head:int=None, action_cnt:int=None, cutting_cnt:int=None) -> None:
        self.row = row
        self.col = col
        self.head = head
        self.action_cnt = action_cnt
        self.cutting_cnt = cutting_cnt

def find_start_pos() -> tuple:
    """
    시작 위치를 발견하는 함수
    """
    for r in range(N):
        for c in range(N):
            if A[r][c] == "X":
                return (r, c)

def solve():
    # 정답(최소 조작 횟수)
    min_control = float('inf')
    
    # 시작 위치 탐색
    start_pos = find_start_pos()

    # 방문 행렬 (3차원)
    # level(나무 베기 횟수) -> row -> col
    visited = [[[0] * N for _ in range(N)] for _ in range(K+1)]

    # BFS
    Q = deque() # ((좌표:tuple), 방향, 조작 횟수)
    car = Car(*start_pos, head=U, action_cnt=0, cutting_cnt=0)
    visited[car.cutting_cnt][car.row][car.col] = 1 # 나무베기 0회, 시작 위치 방문 표시
    Q.append(car)
    
    while Q:
        # 현재 위치 / 방향 / 조작 횟수
        car:Car = Q.popleft()
        r = car.row
        c = car.col
        for nxt_dir, dr, dc in [(U,-1,0), (R,0,1), (D,1,0), (L,0,-1)]:
            nr = r + dr
            nc = c + dc
            # out of index -> continue
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
            
            # already visited -> continue
            if visited[car.cutting_cnt][nr][nc]: continue
            
            # 다음 조작 횟수 = 현재 조작 횟수 + 회전 횟수 + 이동 횟수(1)
            nxt_action_cnt = car.action_cnt + rotate_cnt[car.head][nxt_dir] + 1
            
            # 벌목 횟수
            nxt_cutting_cnt = car.cutting_cnt
            # 목적지 도착시 정답 갱신
            if A[nr][nc] == 'Y':
                min_control = min(min_control, nxt_action_cnt)
                continue
            elif A[nr][nc] == 'T':
                # 나무면 벌목 횟수 1 추가, 단 벌목 제한 횟수 초과 시 다음 단계
                if nxt_cutting_cnt + 1 > K:
                    continue
                nxt_cutting_cnt += 1
            
            # 새로 이동하려는 방향이 이동 가능한 방향이라면(G, X)
            nxt_car = Car(nr, nc, nxt_dir, nxt_action_cnt, nxt_cutting_cnt)
            Q.append(nxt_car)
            visited[nxt_car.cutting_cnt][nxt_car.row][nxt_car.col] = 1           
            
    return min_control

repeat = int(input())
result = []
for test_case in range(1, repeat + 1):
    # N: 필드의 크기, K: 나무를 벨 수 있는 횟수
    N, K = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    
    result.append(f'#{test_case} {solve()}')

for row in result:
    print(row)