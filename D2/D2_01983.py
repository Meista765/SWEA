# import sys; sys.stdin = open('D2/input_01983.txt', 'r', encoding='UTF-8')

T = int(input())
percentage = [0.35, 0.45, 0.20]
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = [[] for _ in range(N)]
    
    for i in range(N):
        scores[i] = list(map(int, input().split()))
    print(scores)
    
    total_scores = [0 for _ in range(N)] 
    
    for i in range(N):
        for j in range(3):
            total_scores[i] += scores[i][j] * percentage[j]
    
    total_scores.sort(reverse=True)
    
    # print(total_scores)
    
    grades = ['' for _ in range(N)] 
    for i in range(10):  # i: 0 ~ 9
        
        