'''
- 문제번호  : 1926
- 문항명    : 간단한 369게임
- 핵심      : 
'''

N = int(input())

for num in range(1, N + 1):
    # 숫자를 문자열로 변환
    num_str = str(num)
    
    # 문자열의 문자가 3, 6, 9 중 하나라면 1을 return하는 list comprehension
    count_369 = sum(1 for char in num_str if char in '369')
    
    # 3, 6, 9 중 하나 이상을 포함한다면,
    if count_369 > 0:
        print('-' * count_369, end=' ')
    else:
        print(num_str, end=' ')