import sys; sys.stdin = open('D2/input_01974.txt')
T = int(input())

def check_sudoku():
    # block check
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            num_lst = []
            for ni in range(i, i+3):
                for nj in range(i, i+3):
                    if A[ni][nj] not in num_lst:
                        num_lst.append(A[ni][nj])
            if len(num_lst) < 9:
                return 0
    
    # row check
    for i in range(N):
        num_lst = []
        for j in range(N):
            if A[i][j] not in num_lst:
                num_lst.append(A[i][j])
        if len(num_lst) < 9:
                return 0
    
    # column check
    for j in range(N):
        num_lst = []
        for i in range(N):
            if A[i][j] not in num_lst:
                num_lst.append(A[i][j])
        if len(num_lst) < 9:
                return 0
    
    return 1

for tc in range(1, T+1):
    N = 9
    A = [list(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {check_sudoku()}')