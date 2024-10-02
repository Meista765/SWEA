import sys; sys.stdin = open('sample_input.txt')

# enum class
ADD, SUB, MUL, DIV = range(4)

def DFS(idx, cur_result):
    global max_result, min_result
    
    # 종료 조건 도달 시, 최소값 갱신
    if idx == N:
        max_result = max(max_result, cur_result)
        min_result = min(min_result, cur_result)
    else:
        for opr in range(4):
            if ops[opr] > 0:
                ops[opr] -= 1 # 연산자 차감
                next_result = cur_result
                if opr is ADD:
                    next_result += nums[idx]
                elif opr is SUB:
                    next_result -= nums[idx]
                elif opr is MUL:
                    next_result *= nums[idx]
                elif opr is DIV:
                    next_result = int(next_result / nums[idx]) # 버림 나눗셈
                
                DFS(idx + 1, next_result)
                ops[opr] += 1 # 연산자 원복

T = int(input())
results = [str()] * T

for tc in range(1, T+1):
    N = int(input())
    
    ops = list(map(int, input().split()))   # 연산자 개수
    nums = list(map(int, input().split()))  # 숫자 배열
    
    min_result = 1<<31
    max_result = -min_result
    
    DFS(1, nums[0])
    
    results[tc-1] = '#{} {}'.format(tc, max_result - min_result)

for result in results:
    print(result)