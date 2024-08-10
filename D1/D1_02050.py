'''
- 문제번호  : 2050
- 문항명    : 알파벳을 숫자로 변환
- 핵심      : ord, chr
'''

word = input().rstrip()

for ch in word:
    print(ord(ch)-ord('A')+1, end=' ')