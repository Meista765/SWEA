'''
- 문제번호  : 2056
- 문항명    : 연월일 달력
- 핵심      : 데이터 슬라이싱
'''

T = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, T+1):
    str_in = input().rstrip()
    
    year    = str_in[0:4]
    month   = str_in[4:6]
    day     = str_in[6:8]
    
    if not (1 <= int(month) <= 12):
        print(f'#{tc} -1')
        continue
    
    if not (1 <= int(day) <= days[int(month)-1]):
        print(f'#{tc} -1')
        continue
    
    print(f'#{tc} {year}/{month}/{day}')