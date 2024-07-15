'''
- 문제번호  : 2063
- 문항명    : 중앙값 찾기
- 핵심      : median 구현
'''

N = int(input())
lst = list(map(int, input().split()))
print(sorted(lst)[N//2])