import sys; sys.stdin = open('D4/input_04008.txt')

T = int(input())

def DFS(k:int, op_lst:str) -> None:
    global min_sum, max_sum
    operator = ['+', '-', '*', '/']
    
    if k == M:
        tmp_sum = numbers[0]
        for i in range(M):
            if op_lst[i] == '+':
                tmp_sum += numbers[i+1]
            elif op_lst[i] == '-':
                tmp_sum -= numbers[i+1]
            elif op_lst[i] == '*':
                tmp_sum *= numbers[i+1]
            elif op_lst[i] == '/':
                tmp_sum //= numbers[i+1]
                # if tmp_sum < 0:
                #     tmp_sum = (tmp_sum // numbers[i+1]) + 1
                # else:
                #     tmp_sum = (tmp_sum // numbers[i+1])
        
        min_sum = min(min_sum, tmp_sum)
        max_sum = max(max_sum, tmp_sum)
    
    for i in range(4):
        if ops_num[i] > 0:
            ops_num[i] -= 1
            DFS(k + 1, op_lst + operator[i])
            ops_num[i] += 1

for tc in range(1, T+1):
    N = int(input()) # 수 개수
    M = N - 1        # 연산자 개수
    
    ops_num = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    
    min_sum = float('inf')
    max_sum = float('-inf')
    DFS(0, '')
    print(f'#{tc} {max_sum - min_sum}')