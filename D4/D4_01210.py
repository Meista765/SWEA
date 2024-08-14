import sys
sys.stdin = open('input.txt', 'r')

T = 10
N = 100

for _ in range(T):
    tc = int(input())

    A = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for column in range(N):  # column of A: 1 ~ N(100)
        i = 0
        j = column
        if A[0][j] != 1:  # 첫 행의 요소가 1이 아니면 다음 탐색
            continue

        while i < N-1:  # loop until i reach N-1(99)
            i += 1  # go down

            if (j+1 < N) and (A[i][j+1] == 1):
                while (j+1 < N) and (A[i][j+1] == 1):  # check weather "right" is available
                    j += 1
            elif (j-1 >= 0) and (A[i][j-1] == 1):
                while (j-1 >= 0) and (A[i][j-1] == 1):  # check weather "left" is available
                    j -= 1

        # print(f'column: {column}, j: {j}')
        if A[i][j] == 2:  # if end value is 2,
            ans = column
            break

    print(f'#{tc} {ans}')