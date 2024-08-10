T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    prices = list(map(int, input().split()))
    
    profits = 0
    while len(prices) > 0:
        max_price = max(prices)
        max_idx = prices.index(max_price)
        for price in prices[:max_idx]:
            profits += (max_price - price)
        prices = prices[max_idx+1:]
    
    print(f'#{test_case} {profits}')