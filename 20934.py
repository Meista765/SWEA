import sys
sys.stdin = open("input.txt", 'r')

T = int(input())

for tc in range(1, T + 1):
    S, K = input().split()
    K = int(K)

    ans = 0
    idx = S.index('o')

    # o..의 경우
    if idx == 0:
        if K == 0:
            ans = 0
        elif K % 2 == 0:
            ans = 0
        else:
            ans = 1

    # .o.의 경우
    elif idx == 1:
        # .o.는 0인 케이스가 불가하다
        if K % 2 == 0:
            ans = 1
        else:
            ans = 0

    # ..o의 경우
    elif idx == 2:
        if K == 0:
            ans = 2
        elif K % 2 == 0:
            ans = 0
        else:
            ans = 1


    print(f'#{tc} {ans}')