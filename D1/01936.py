'''
- 문제번호  : 1936
- 문항명    : 1대1 가위바위보
- 핵심      : 
'''
B_win = [(1,2), (2,3), (3,1)]

if tuple(map(int, input().split())) in B_win:
    print("B")
else:
    print("A")
