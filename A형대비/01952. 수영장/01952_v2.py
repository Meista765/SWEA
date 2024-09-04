import sys; sys.stdin = open('./01952. 수영장/input.txt')

def find_candidates(cur_sum, k = 1, start = 0):
    if k == 4:
        return
    else:
        for i in range(start, 12 - 2):
            # 오른쪽으로 두 칸 모두 방문한 적이 없으면,
            if not visited[i] and not visited[i+1] and not visited[i+2]:
                visited[i] = visited[i+1] = visited[i+2] = 1
                
                # 가지치기: 새로 구한 합계가 기존 합계보다 커지면(악화되면) 해당 노드 탐색을 중단한다.
                new_sum = cur_sum - plan[i] - plan[i+1] - plan[i+2] + prices[Q]
                if new_sum > cur_sum:
                    visited[i] = visited[i+1] = visited[i+2] = 0
                else:
                    candidates.add(new_sum)
                    # 다음 탐색(인덱스는 + 3)
                    find_candidates(new_sum, k + 1, i + 3)
                    visited[i] = visited[i+1] = visited[i+2] = 0

T = int(input())

for tc in range(1, T+1):
    D, M, Q, Y = range(4)  # 일, 월, 분기, 년
    prices = list(map(int, input().split()))
    
    plan = list(map(int, input().split()))
    
    # 일권 또는 월권으로 끊었을 때 저렴한 가격을 저장
    for i in range(12):
        if plan[i]:
            plan[i] = min(plan[i] * prices[D], prices[M])
    
    # 후보군 초기화
    # 1. 계획이 있는 달은 일권 또는 달권으로 구매한 가격 중 저렴한 쪽을 선택
    # 2. 1년권
    # 3. 분기권 * 4
    
    candidates = set([
        sum(plan), 
        prices[Q] * 4, 
        prices[Y]
    ])
    
    # 4. 분기권으로 가렸을 때 이득인 구간을 가린 값
    visited = [0] * 12
    find_candidates(sum(plan))
    
    # # 디버그용
    # print('plan: ', *plan)
    # print(candidates)
    # print('최소값: ', min(candidates))
    # print()
    
    print('#{} {}'.format(tc, min(candidates)))