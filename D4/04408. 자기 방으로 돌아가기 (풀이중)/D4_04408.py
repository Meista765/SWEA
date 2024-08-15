import sys; sys.stdin = open('D4/input_04408.txt')

def scheduling():
    global A
    # 점유 중인 시간이 짧은 것 우선, 종료시간이 빠른 것 우선 정렬
    A = sorted(A, key=lambda x: (x[1], x[1] - x[0]))
    
    step = 0
    while A:
        # 이용중인 복도를 나타내는 배열
        occupied = [False] * 401  # 0번은 dummy
        
        # 현재 보유중인 데이터에 대해서 1회 순회
        for _ in range(len(A)):
            data = A.pop(0)
            start = data[0]
            end = data[1]
            
            for idx in range(start, end+1):  # idx: start ~ end
                # 복도가 이용중이라면 데이터 원복
                if occupied[idx]: 
                    A.append(data)
                    break
            # 이용중이 아니라면, 이용 표시 후 데이터 소비
            else:
                for idx in range(start, end+1):  # idx: start ~ end
                    occupied[idx] = True
        
        step += 1
    
    return step


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    
    print(f'#{tc} {scheduling()}')