import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    A = [[0 for _ in range(10)] for _ in range(10)]
    
    cnt = 0
    for _ in range(int(input())):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2+1): # x: x1 ~ x2
            for y in range(y1, y2+1): # y: y1 ~ y2
                A[x][y] += color
                if A[x][y] == 3: # red(1) + blue(2) = purple(3)
                    cnt +=1
    
    print(f'#{tc} {cnt}')