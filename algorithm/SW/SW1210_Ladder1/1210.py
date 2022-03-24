import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)]  # 2차원 사다리 배열
    n = len(arr)  # arr = n * n

    # 도착지점 찾기
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start = [i, j]  # [9, 9]

    # 우좌상 : 아래로 내려가지 X
    di = [0, 0, -1]
    dj = [1, -1, 0]
    row = start[0]
    col = start[1]

    while row != 0:  # row = 0 : 도착점
        me = arr[row][col]  # 현재 내 위치
        for k in range(3):
            ni = row + di[k]
            nj = col + dj[k]

            if 0 <= ni < n and 0 <= nj < n:
                r = arr[ni][nj]

                if r == 1:  # 1이 있으면 이동하기
                    row = ni
                    col = nj
                    arr[ni][nj] -= 1  # 이동했을 경우 그 값을 0으로 만들기
                    break

    print(f'#{tc} {col}')