import sys; sys.stdin = open('D2/12386. 숫자카드/input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, list(input())))

    card_lst = [0] * 10
    for card in A:
        card_lst[card] += 1
    
    max_num = -1
    max_cnt = -1
    for card in range(10):
        if card_lst[card] >= max_cnt:
            max_num = card
            max_cnt = card_lst[card]

    print('#{} {} {}'.format(tc, max_num, max_cnt))