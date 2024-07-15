'''
- 문제번호 : 2068
- 문항명   : 최대수 구하기
'''

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    print(f'#{tc} {max(lst)}')