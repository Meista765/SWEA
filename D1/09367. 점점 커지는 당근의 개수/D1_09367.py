import sys; sys.stdin = open('D1/input_09367.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    
    max_cnt = float('-inf')
    cnt = 0
    prev = 0
    for num in A:
        if prev > num:
            max_cnt = max(max_cnt, cnt)
            cnt = 0
        prev = num
        cnt += 1
    max_cnt = max(max_cnt, cnt)
    
    print(f'#{tc} {max_cnt}')