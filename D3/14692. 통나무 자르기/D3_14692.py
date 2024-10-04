# import sys; sys.stdin = open('')
T = int(input())
results = [str()] * T

for tc in range(1, T+1):
    N = int(input())
    
    if N & 1:
        results[tc - 1] = f'#{tc} Bob'
    else:
        results[tc - 1] = f'#{tc} Alice'

for result in results:
    print(result)