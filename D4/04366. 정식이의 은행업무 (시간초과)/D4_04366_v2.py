# import sys; sys.stdin = open('D4/input_04366.txt')
from itertools import product

def solve():
    for idx_bin, idx_tri in product(range(len(binary)), range(len(trinary))):
        tmp_bin = binary[idx_bin]
        tmp_tri = trinary[idx_tri]
        
        for digit_bin, digit_tri in product(range(2), range(3)):
            if tmp_bin == str(digit_bin) or tmp_tri == str(digit_tri):
                continue
            
            binary[idx_bin] = str(digit_bin)
            trinary[idx_tri] = str(digit_tri)
            
            if int(''.join(binary), 2) == int(''.join(trinary), 3):
                return int(''.join(binary), 2)
        
        binary[idx_bin] = tmp_bin
        trinary[idx_tri] = tmp_tri

T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    trinary = list(input())
    
    print(f'#{tc} {solve()}')