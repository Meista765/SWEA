T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    print(f'#{tc} {round(sum(lst)/len(lst))}')