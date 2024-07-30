T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 건물 수(강물 포함)
    A = list(map(int, input().split())) # 높이 정보

    first_max = 0 # 가장 큰 수
    second_max = 0 # 두 번째로 큰 수
    
    def change_max(num):
        '''가장 큰 수와 두 번째로 큰 수를 수정하는 함수'''
        global first_max, second_max
        if num >= first_max:
            second_max = first_max
            first_max = num
    
    def remove_and_add(rm, ad):
        '''슬라이딩 윈도우를 한 칸 전진시키면서 '''
    
    idx = 2 # 탐색 인덱스
    # 슬라이딩 윈도우 초기화
    for i in range(2, 5): # i: 2 ~ 4
        change_max(A[i])
    
    
    
    print(f'#{tc} {max_diff}')