import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/SSAFY_12th/02. Algorithm Basic/24-07-30-Tue/input.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    # 각 tc에 해당하는 더미 변수 흡수
    input()
    
    num_lst = map(int, input().split())
    
    # 최빈값을 저장하는 딕셔너리
    frequency = [0] * 101
    for num in num_lst:
        frequency[num] += 1
    
    # 최대 최빈값과 해당 수가 저장된 index를 갱신
    mode = 0
    ans = 0
    for i in reversed(range(101)): # i: 0 ~ 100
        if frequency[i] > mode:
            mode = frequency[i]
            ans = i
    
    print(f'#{tc} {ans}')