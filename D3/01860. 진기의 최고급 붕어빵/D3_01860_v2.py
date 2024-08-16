import sys; sys.stdin = open('D3/input_01860.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    
    # 손님 방문시간 확인
    customer_lst = list(map(int, input().split()))
    last_customer = max(customer_lst)
    
    # 방문 시간대별 수요 조사
    demand = [0] * (last_customer + 1)
    for customer in customer_lst:
        demand[customer] += 1
    
    answer = 'Possible'
    # 잔여 붕어빵 수
    remaining_taiyaki = -K
    # 시간 증가
    for cur_time in range(last_customer + 1):  # cur_time = 0 ~ last_customer
        # 매 M마다 붕어빵 추가
        if cur_time % M == 0:
            remaining_taiyaki += K
        
        # 잔여 붕어빵에서 수요만큼 제거
        remaining_taiyaki -= demand[cur_time]
        
        # 잔여 붕어빵이 모자라면 에러
        if remaining_taiyaki < 0:
            answer = 'Impossible'
            break
    
    print(f'#{tc} {answer}')