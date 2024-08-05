import sys; sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [[0]*N for _ in range(N)]

    # 배열 제작
    for i in range(N):
        cmd = input()
        for j in range(N):
            if cmd[j] == 'o':
                A[i][j] = 1

    # 세로 방향 탐색
    def check_vertical(pos_i:int, pos_j:int) -> bool:
        global A
        ni = pos_i
        # 세로로 5개가 있는지 확인
        for dj in range(5):
            nj = pos_j + dj
            if nj >= N or A[ni][nj] == 0:
                return False
        else:
            return True

    # 가로 방향 탐색
    def check_horizontal(pos_i:int, pos_j:int) -> bool:
        global A
        nj = pos_j
        # 가로로 5개가 있는지 확인
        for di in range(5):
            ni = pos_i + di
            if ni >= N or A[ni][nj] == 0:
                return False
        else:
            return True

    # 우하향 대각 방향 탐색
    def check_diagonal(pos_i:int, pos_j:int) -> bool:
        global A
        # 대각 방향으로 5개가 있는지 확인
        for d in range(5):
            ni = pos_i + d
            nj = pos_j + d
            # OutOfIndex 또는 탐색 위치의 데이터가 0인 경우
            if ni >= N or nj >= N or A[ni][nj] == 0:
                return False
        else:
            return True

    # 좌하향 대각 방향 탐색
    def check_rdiagonal(pos_i:int, pos_j:int) -> bool:
        global A
        # 대각 방향으로 5개가 있는지 확인
        for d in range(5):
            ni = pos_i + d
            nj = pos_j - d
            # OutOfIndex 또는 탐색 위치의 데이터가 0인 경우
            if ni >= N or nj < 0 or A[ni][nj] == 0:
                return False
        else:
            return True

    found = False  # 이중 for-문을 빠져나가기 위한 flag
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                found |= check_diagonal(i, j)
                found |= check_rdiagonal(i, j)
                found |= check_horizontal(i, j)
                found |= check_vertical(i, j)
            if found:
                break
        if found:
            break

    if found:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')