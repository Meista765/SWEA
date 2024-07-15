T = int(input())

for tc in range(1, T+1):
    lst = map(int, input().split())
    print(f'#{tc} {sum([num for num in lst if num % 2 == 1])}')