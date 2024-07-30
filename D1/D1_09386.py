T = int(input())

for tc in range(1, T+1):
    N = int(input())
    in_str = input().rstrip()
    
    max_cnt = float('-inf')
    cnt = 0
    for ch in in_str:
        if ch == '0':
            if cnt > max_cnt: max_cnt = cnt
            cnt = 0
            
        elif ch == '1':
            cnt += 1
    
    if cnt > max_cnt: max_cnt = cnt
    
    print('#{} {}'.format(tc, max_cnt))