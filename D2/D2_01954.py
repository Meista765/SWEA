import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = [[0 for _ in range(N)] for _ in range(N)]

    num = 1  # count to put in to array
    i, j = 0, -1  # initialize index
    loops = 0
    signs = [1, -1]  # when loops is even -> plus, loops is odd -> minus
    for n in reversed(range(1, N+1)):  # n: N ~ 1
        # move horizontal
        for _ in range(n):
            j += signs[loops % 2] * 1
            A[i][j] = num
            num += 1

        # move vertical
        for _ in range(n-1):
            i += signs[loops % 2] * 1
            A[i][j] = num
            num += 1

        loops += 1

    print(f'#{tc}')
    for row in A:
        print(*row)