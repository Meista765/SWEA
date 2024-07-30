T = int(input())

def find_idx(lst:list, mode:str) -> int:
    if not lst:
        return lst

    tmp = lst[0]
    idx = 0
    
    for i in range(1, len(lst)):
        if mode == 'max' and lst[i] >= tmp:
            tmp = lst[i]
            idx = i
        elif mode == 'min' and lst[i] < tmp:
            tmp = lst[i]
            idx = i
    
    return idx

for tc in range(1, T+1):
    N = map(int, input().split())
    A = list(map(int, input().split()))
    
    print('#{} {}'.format(tc, abs(find_idx(A,'max') - find_idx(A,'min'))))