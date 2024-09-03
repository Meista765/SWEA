import sys; sys.stdin = open('A형대비/01952. 수영장/input.txt')

def find_candidates(k = 1, start = 0):
    if k == 4:
        return
    else:
        for i in range(start, 12 - 3):
            # 값이 있는 셀에서부터 오른쪽으로 두 칸 모두 방문한 적이 없으면,
            if plan[i] and not visited[i] and not visited[i+1] and not visited[i+2]:
                visited[i] = visited[i+1] = visited[i+2] = 1
                # 계산
                tmp_sum = k * prices[Q] + sum(plan[idx] for idx in range(12) if not visited[idx])
                
                visited[i] = visited[i+1] = visited[i+2] = 0

T = int(input())

for tc in range(1, T+1):
    D, M, Q, Y = range(4)  # 일, 월, 분기, 년
    prices = list(map(int, input().split()))
    
    plan = list(map(int, input().split()))
    
    # 일권 또는 월권으로 끊었을 때 저렴한 가격을 저장
    for i in range(12):
        if plan[i]:
            plan[i] = max(plan[i] * prices[D], prices[M])
    
    # 후보군 생성
    # 1. 일권과 월권을 섞어서 최소가 되는 값
    # 2. 1년권
    # 3. 분기권 * 4
    # 4. 분기권으로 가렸을 때 이득인 구간을 가린 값
    
    candidates = [sum(plan), prices[Q] * 4, prices[Y]]
    
    visited = [0] * 12
    
    print(candidates)