'''
- 문제번호  : 2070
- 문항명    : 큰 놈, 작은 놈, 같은 놈
- 핵심      : 삼항 연산자(Ternary operators)
'''

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())
    ans = '<' if a < b else ('=' if a == b else '>')
    print(f'#{tc} {ans}')