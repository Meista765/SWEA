import sys; sys.stdin = open('input_04366.txt')

# 10진수를 N진수로 변경하는 함수
def toBaseN(num, base):
    result = ''
    while num:
        num, remainder = divmod(num, base)
        result += str(remainder)

    return int(result[::-1])

# N진수인 두 수 사이의
def diffCheck(num1, num2):
    if num1 == num2:
        return False

    cnt = 0
    for digit_1, digit_2 in zip(list(str(num1)), list(str(num2))):
        if digit_1 != digit_2:
            cnt += 1
        if cnt > 1:
            break

    if cnt == 1:
        return True
    else:
        return False

T = int(input())

for tc in range(1, T+1):
    binary = int(input())
    trinary = int(input())

    # 2진수, 3진수의 자릿수
    digit_bin = len(str(binary))
    digit_tri = len(str(trinary))
    
    '''
    2진수가 4자리, 3진수가 3자리라고 하자.
    상한 = 10000(2진수), 1000(3진수) 중에 작은 것
    하한 = 1000(2진수), 100(3진수) 중에 큰 것
    ''' 
    upperBound = min(2 ** digit_bin, 3 ** digit_tri)
    lowerBound = max(2 ** (digit_bin - 1), 3 ** (digit_tri - 1))

    for num in range(lowerBound, upperBound):
        if diffCheck(toBaseN(num, 2), binary) & diffCheck(toBaseN(num, 3), trinary):
            # print('2진수 원본: {}, 변경 후: {}'.format(binary, toBaseN(num, 2)))
            # print('3진수 원본: {}, 변경 후: {}'.format(trinary, toBaseN(num, 3)))
            print(f'#{tc} {num}')
            break