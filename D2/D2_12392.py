import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1): # tc: 1 ~ T
    N = int(input())
    A = list(map(int, input().split()))

    # 입력 정렬
    A.sort()

    ans = f'#{tc} '
    # index에 따라 출력
    for i in range(10): # i: 0 ~ N-1
        if i % 2 == 0: # 짝수
            ans += f'{A[N-1 - i//2]} '
        else: # 홀수
            ans += f'{A[i//2]} '

    print(ans)
