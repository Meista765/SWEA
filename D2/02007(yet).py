'''
- 문제번호  : 2007
- 문항명    : 패턴 마디의 길이
- 핵심      : 
'''

import sys
sys.stdin = open("C:\\Users\\wns95\\Downloads\\input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    phrase = input().rstrip()
    
    # 정답을 저장하는 변수
    answer = 0
    
    # 1부터 입력 길이까지 패턴을 쪼개서 검사
    for pattern_len in range(1, len(phrase)):
        # Parsing
        pattern = phrase[0:pattern_len]
        
        # 패턴 길이와 동일하게 문자열을 잘라서 검토
        slicer = pattern_len
        count = 0
        while slicer < len(phrase):
            if pattern in phrase[slicer:]:
                count += 1
            slicer += pattern_len
        
        if count > 1:
            answer = count
    
    print(f'#{tc} {answer}')