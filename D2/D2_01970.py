T = int(input())

# 화폐 단위
moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    paid = int(input()) # 지불 금액
    counts = [0] * len(moneys) # 거스름돈 카운트
    
    for i, money in enumerate(moneys): # (0, 50000), (1, 10000), (2, 5000), ...
        while paid >= money: # 탈출 조건: paid < money == 거슬러 주려는 돈이 지불한 돈보다 클 때
            counts[i] += 1
            paid -= money
    
    print('#{}'.format(tc))
    print(*counts)