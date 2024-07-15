'''
- 문제번호  : 2058
- 문항명    : 자릿수 더하기
'''

N = int(input())
ans = 0
while N > 0:
    ans += N % 10
    N = N // 10
print(ans)