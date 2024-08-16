import sys; sys.stdin = open('D3/input_01860.txt')

def taiyaki():
    cur_time = 0    # 현재 시각
    taiyaki_rem = 0 # 남은 붕어빵
    rem_demand = sum(demand)
    while cur_time < data_size:
        cur_time += 1
        
        # 쿨타임이 돌면 붕어빵 개수 충전
        if cur_time % cooltime == 0:
            taiyaki_rem += taiyaki_making_cnt
        
        taiyaki_rem -= demand[cur_time]
        rem_demand -= demand[cur_time]
        
        if taiyaki_rem < 0:
            return 'Impossible'
        
        if rem_demand == 0:
            break

    
    return 'Possible'

T = int(input())
for tc in range(1, T+1):
    input_size, cooltime, taiyaki_making_cnt = map(int, input().split())
    
    data_size = 11111
    demand = [0] * (data_size + 1)  # index에 해당하는 시간에 필요로 하는 붕어빵의 개수; 0번은 dummy
    
    # 수요 배열 제작
    ETAs = list(map(int, input().split()))
    for ETA in ETAs:
        demand[ETA] += 1
    
    print(f'#{tc} {taiyaki()}')