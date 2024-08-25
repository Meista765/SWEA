import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/SSAFY_12th/02. Algorithm Basic/24-07-30-Tue/input.txt", 'r')
# 투 포인터 & 카운팅

for tc in range(1, 11): # tc: 1 ~ 10
    dump = int(input()) # 덤프 제한 수
    num_lst = list(map(int, input().split())) # 입력 수 리스트
    
    freq = [0] * 101 # 각 수의 빈도를 저장하는 배열 / idx: 0 ~ 100
    # 빈도 계산
    for num in num_lst:
        freq[num] += 1
    
    # 최소값과 최대값을 저장하는 변수
    max_val = 100
    min_val = 1
    
    # freq 리스트 내의 0이 아닌 수를 만나면 idx 갱신
    # 최소값 갱신
    for i in range(1, 101): # i: 1 ~ 100
        if freq[i] != 0:
            min_val = i
            break
    
    # 최대값 index 갱신
    for i in reversed(range(1, 101)): # i: 100 ~ 1
        if freq[i] != 0:
            max_val = i
            break
    
    # dump 횟수 제한 한도만큼 탐색
    for _ in range(dump): # loop {dump} times
        # 더 이상 바꿀 것이 없는 상태
        if not min_val+1 < max_val-1:
            break
        
        freq[min_val] -= 1
        freq[min_val+1] += 1
        
        freq[max_val] -= 1
        freq[max_val-1] += 1
        
        if not freq[min_val]: min_val += 1
        if not freq[max_val]: max_val -= 1
    
    print('#{} {}'.format(tc, max_val - min_val))