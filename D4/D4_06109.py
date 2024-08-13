import sys; sys.stdin = open('input_06109.txt', encoding='UTF-8')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, cmd = input().split()
    N = int(N)

    A = [list(map(int, input().split())) for _ in range(N)]
    queue = deque()

    if cmd == 'up':
        for j in range(N):
            for i in range(N):
                if A[i][j] != 0:
                    queue.append(A[i][j])
            i = 0
            while i < N:
                if queue:
                    A[i][j] = queue.popleft()
                    if queue and queue[0] == A[i][j]:
                        A[i][j] += queue.popleft()
                else:  # not queue
                    A[i][j] = 0
                i += 1
    elif cmd == 'down':
        for j in range(N):
            for i in reversed(range(N)):
                if A[i][j] != 0:
                    queue.append(A[i][j])
            i = N-1
            while i > -1:
                if queue:
                    A[i][j] = queue.popleft()
                    if queue and queue[0] == A[i][j]:
                        A[i][j] += queue.popleft()
                else:  # not queue
                    A[i][j] = 0
                i -= 1
    elif cmd == 'left':
        for i in range(N):
            for j in range(N):
                if A[i][j] != 0:
                    queue.append(A[i][j])
            j = 0
            while j < N:
                if queue:
                    A[i][j] = queue.popleft()
                    if queue and queue[0] == A[i][j]:
                        A[i][j] += queue.popleft()
                else:  # not queue
                    A[i][j] = 0
                j += 1
    elif cmd == 'right':
        for i in range(N):
            for j in reversed(range(N)):
                if A[i][j] != 0:
                    queue.append(A[i][j])
            j = N - 1
            while j > -1:
                if queue:
                    A[i][j] = queue.popleft()
                    if queue and queue[0] == A[i][j]:
                        A[i][j] += queue.popleft()
                else:  # not queue
                    A[i][j] = 0
                j -= 1

    print(f'#{tc}')
    for row in A:
        print(*row)


