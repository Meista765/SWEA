import sys
sys.stdin = open('sample_input.txt', 'r')

# 비트 마스크

T = int(input())
A = list(range(1, 13)) # 1 ~ 12

for tc in range(1, T+1):
    size_of_subset, target = map(int, input().split())
    cnt = 0
    
    for bit in range(1 << 12): # i: 0 ~ 2^12-1(4095, 12bit)
        subset = []
        for idx in range(12):
            # bit-masking
            if bit & (1<<idx):
                subset.append(A[idx])
        if len(subset) == size_of_subset and sum(subset) == target:
            cnt += 1
    
    print(f'#{tc} {cnt}')