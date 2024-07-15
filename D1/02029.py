'''
- 문제번호  : 2029
- 문항명    : 몫과 나머지 출력하기
- 핵심      : 
'''

T = int(input())

for tc in range(1, T+1):
    A, B = map(int, input().split())
    print(f'#{tc} {A//B} {A%B}')