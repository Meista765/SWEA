import sys

sys.stdin = open("D2/22654. 차윤이의 RC카/sample_input.txt")

U, R, D, L = range(4)
ROW, COL = range(2)
delta = {U: (-1, 0), R: (0, 1), D: (1, 0), L: (0, -1)}


class Car:
    def __init__(self) -> None:
        self.row, self.col = self._find_start_pos()
        self.orient = U

    def _find_start_pos(self):
        for r in range(N):
            for c in range(N):
                if arr[r][c] == 'X':
                    return (r, c)
    
    def rotate(self, rotate):
        if rotate == "L":
            self.orient = (self.orient - 1) % 4
        elif rotate == "R":
            self.orient = (self.orient + 1) % 4

    def move(self):
        self.row += delta[self.orient][ROW]
        self.col += delta[self.orient][COL]

        # out-of-index
        if self.row < 0 or self.row >= N or self.col < 0 or self.col >= N:
            return False

        # 나무
        if arr[self.row][self.col] == "T":
            return False

        return True


T = int(input())
results = [str()] * T

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    
    results[tc-1] += f'#{tc}'
    
    for _ in range(int(input())):
        number, commends = input().split()
        car = Car()
        
        for commend in commends:
            if commend == 'A':
                if car.move():
                    
        
