import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1): # tc: 1 ~ T
    pages, a_page, b_page = map(int, input().split())

    A = list(range(pages+1)) # 0 ~ pages

    def binary_search(lo, hi, tgt, depth) -> int:
        '''
        :param lo: 왼편 index
        :param hi: 오른편 index
        :param tgt: 찾고자 하는 수
        :param depth: binary search가 재귀적으로 호출된 횟수
        :return: depth
        '''
        if lo > hi: # Not found
            return float('inf')

        # 중앙값
        mid = (lo + hi) // 2
        depth += 1

        if A[mid] == tgt:
            return depth
        elif A[mid] > tgt:
            return binary_search(lo, mid-1, tgt, depth)
        else: # A[mid] < tgt:
            return binary_search(mid+1, hi, tgt, depth)

    result_a = binary_search(1, pages, a_page, 1)
    result_b = binary_search(1, pages, b_page, 1)
    if result_a < result_b:
        print(f'#{tc} A')
    elif result_a > result_b:
        print(f'#{tc} B')
    else: # result_a == result_b
        print(f'#{tc} 0')