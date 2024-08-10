'''
- 문제번호  : 2005
- 문항명    : 파스칼의 삼각형
- 핵심      : 
'''

import sys
sys.stdin = open("C:\\Users\\wns95\\Downloads\\input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    print(f'#{tc}')
    
    N = int(input())
    
    # 이전에 탐색한 결과물을 저장하는 리스트 
    lst_prev = [1]
    
    for i in range(N):
        lst_now = []
    