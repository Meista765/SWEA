T = int(input())

def bubble_sort(lst:list) -> list:
    for i in reversed(range(len(lst))): # i: N-1 ~ 0
        for j in range(i): # j: 0 ~ i-1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst

for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(set(map(int, input().split())))
    
    A = bubble_sort(A)
    
    print(f'#{tc} {A[K-1]}')