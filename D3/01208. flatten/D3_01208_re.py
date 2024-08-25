import sys; sys.stdin = open('D3/01208. flatten/input.txt')

for tc in range(1, 11):
    dump = int(input())
    num_lst = list(map(int, input().split()))
    
    cnt_lst = [0] * (max(num_lst) + 1)
    
    for number in num_lst:
        cnt_lst[number] += 1
    
    start = 0
    end = max(num_lst)
    while dump > -1 and end - start > 1:
        while not cnt_lst[start]:
            start += 1
        
        while not cnt_lst[end]:
            end -= 1
        
        gap = min(cnt_lst[start], cnt_lst[end])
        
        if dump < gap:
            break
        else:
            cnt_lst[start] -= gap
            cnt_lst[start + 1] += gap
            cnt_lst[end] -= gap
            cnt_lst[end - 1] += gap
            dump -= gap
    
    print('#{} {}'.format(tc, end - start))