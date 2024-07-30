import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 입력 개수(N), 정훈이 키(B)
    N, B = map(int, input().split())
    
    # 점원 입력
    heights = list(map(int, input().split()))
    heights = sorted(heights)
    
    # 부분합 생성
    subSum = []
    for i, h in enumerate(heights):
        if i == 0: subSum.append(h)
        else: subSum.append(h + subSum[i-1])
    
    idxL = 0
    idxR = N-1
    ans = subSum[idxR]
    while idxL < idxR:
        # 키 합계에서 구성원의 키를 뺐을 때 영향이 작은 방향으로 탐색
        if heights[idxL] <= heights[idxR]:
            idxL += 1
        else:
            idxR -= 1
        # 차이 계산
        diff = subSum[idxR] - subSum[idxL]
        # 차이가 조건에 부합하면 갱신, 그렇지 않으면 반복 종료
        if diff >= B:
            ans = diff
        else:
            break
    
    print(f'#{tc} {ans - B}')