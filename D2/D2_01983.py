import sys; sys.stdin = open('D2/input_01983.txt', 'r', encoding='UTF-8')
# TEST = True

T = int(input())
percentage = [0.35, 0.45, 0.20]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = [[] for _ in range(N)]
    
    for i in range(N):
        scores[i] = list(map(int, input().split()))
    
    # 총점, idx, 학점
    total_scores = [[0, 0, str()] for _ in range(N)] 
    
    for i in range(N):
        total_scores[i][1] = i
        for j in range(3):
            total_scores[i][0] += scores[i][j] * percentage[j]
    
    total_scores.sort(reverse=True)
    
    
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for n in range(10):  # i: 0 ~ 9
        step = N // 10
        for i in range(step * n, step * (n+1)):
            if i < N:
                total_scores[i][2] = grade[n]
    
    total_scores.sort(key=lambda x: x[1])
    
    # print(total_scores)
    
    print(f'#{tc} {total_scores[K-1][2]}')