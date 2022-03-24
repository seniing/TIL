import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    # 행과 열 검사
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(arr[i][j])
            col.append(arr[j][i])
        if len(set(row)) < 9 or len(set(col)) < 9:
            ans = 0

    # 3*3 영역 검사
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            nine = []
            for k in range(3):
                for l in range(3):
                    nine.append(arr[i+k][j+l])
            if len(set(nine)) < 9:
                ans = 0

    print(f'#{tc} {ans}')
