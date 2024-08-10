T = int(input())

# tc: test case
for tc in range(1, T+1):
    # 입력 데이터를 저장
    lst = list(map(int, input().split()))
    
    '''
    필터링 (List Comprehension)
    1. lst 내의 객체를 num으로 저장
    2. num을 2로 나눈 나머지가 1인 경우(홀수)에만 리스트에 저장
    '''
    lst = [num for num in lst if num % 2 == 1]
    
    # lst에 담긴 내용을 저장
    print(f'#{tc} {sum(lst)}')