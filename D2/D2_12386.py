T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, list(input())))
    
    freq = [0] * 10 # idx: 0 ~ 9
    
    for num in A:
        freq[num] += 1
    
    card = -1 # card에 적힌 수를 저장하는 변수
    max_cnt = -1 # card의 개수를 저장하는 변수
    # 역순으로 탐색
    for i in reversed(range(10)): # i: 9 ~ 0
        # 최대 개수를 새로 발견하면 갱신
        if freq[i] > max_cnt:
            card = i
            max_cnt = freq[i]
    
    print('#{} {} {}'.format(tc, card, max_cnt))