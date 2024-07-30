import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # factors
    factor = [2, 3, 5, 7, 11]
    
    # 2, 3, 5, 7, 11의 승수를 저장하는 리스트
    factorized = []
    
    number = int(input())
    for divisor in factor:
        cnt = 0
        while number % divisor == 0:
            number //= divisor
            cnt += 1
        factorized.append(cnt)
    
    print(f'#{tc}', end=' ')
    print(*factorized)