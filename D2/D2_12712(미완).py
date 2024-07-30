import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # 배열 크기(N), 살충제 범위(M) 입력
    N, M = map(int, input().split())
    
    # 파리 배열 입력
    lst = [list(map(int, input().split())) for _ in range(N)]
    
    # 정답 초기화
    ans = 0
    
    for i in range(N):
        for j in range(N):
            # 십자 방향 데이터 저장
            tmp_plus = lst[i][j]
            # 좌우 방향
            for d in range(-M + 1, M):
                jj = j + d
                # 인덱스 범위가 접근 가능 범위를 벗어나는 경우 skip
                if (jj < 0) or (jj >= M):
                    continue
                # 탐색중인 위치와 동일한 경우 skip
                if (j == jj):
                    continue
                #위 두 경우에 해당되지 않는다면
                tmp_plus += lst[i][jj]
            # 상하 방향
            for d in range(-M + 1, M):
                ii = i + d
                # 인덱스 범위가 접근 가능 범위를 벗어나는 경우 skip
                if (ii < 0) or (ii >= M):
                    continue
                # 탐색중인 위치와 동일한 경우 skip
                if (i == ii):
                    continue
                #위 두 경우에 해당되지 않는다면
                tmp_plus += lst[ii][j]
            
            # 대각선 방향 데이터 합계
            tmp_cross = lst[i][j]
            for d in range(-M + 1, M):
                # 우하향
                ii, jj = i + d, j + d
                if (ii < 0) or (ii >= M) or (jj < 0) or (jj >= M):
                    continue
                if i == ii and j == jj:
                    continue
                tmp_cross += lst[ii][jj]
                
                # 우상향
                ii = i - d
                if (ii < 0) or (ii >= M) or (jj < 0) or (jj >= M):
                    continue
                if i == ii and j == jj:
                    continue
                tmp_cross += lst[ii][jj]
            ans = max(ans, tmp_cross, tmp_plus)

    print(f'#{tc} {ans}')