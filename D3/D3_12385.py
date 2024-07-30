T = int(input())

for tc in range(1, T+1):
    max_step, station_cnt, charger_cnt = map(int, input().split())
    
    # 충전기 위치: 1이 충전기 있음
    charger_loc = [0] * (station_cnt + max_step) # idx: 0 ~ M+K-1
    
    # 충전기 위치 수정
    A = list(map(int, input().split()))
    for i in A:
        charger_loc[i] = 1
    
    # 현재 위치
    pos_now = max_step
    # 들린 충전소 수
    cnt = 0
    
    # 종점에 도착하면 반복 종료
    while pos_now < station_cnt: # 종료조건: pos_now >= station_cnt
        # 갈 수 있는 최대 위치까지 가본다
        for dx in range(max_step): # dx: 0 ~ K-1
            if charger_loc[pos_now - dx]:
                pos_now = pos_now - dx
                cnt += 1
                break
        else: # 도중에 충전소를 못만난 경우
            cnt = 0 # 실패
            break # break while-loop
        pos_now += max_step
    
    print('#{} {}'.format(tc, cnt))