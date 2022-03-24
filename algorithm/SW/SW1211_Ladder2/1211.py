import sys
sys.stdin = open('input.txt')


def count_ladder(arr, start):
    # 우좌상 : 아래로 내려가지 X
    di = [0, 0, -1]
    dj = [1, -1, 0]
    row = start[0]
    col = start[1]
    count = 0

    # 기존의 값이 바뀌지 않도록 복사
    arr_new = []
    for i in arr:
        arr_new.append(i[:])

    while row != 0:  # row = 0 : 도착점
        me = arr_new[row][col]  # 현재 내 위치
        for k in range(3):
            ni = row + di[k]
            nj = col + dj[k]

            if 0 <= ni < n and 0 <= nj < n:
                r = arr_new[ni][nj]

                if r == 1:  # 1이 있으면 이동하기
                    row = ni
                    col = nj
                    arr_new[ni][nj] -= 1  # 이동했을 경우 그 값을 0으로 만들기
                    count += 1
    return count, col


T = 10
for tc in range(1, T+1):
    N = input()
    arr1 = [list(map(int, input().split())) for _ in range(100)]  # 2차원 사다리 배열
    n = len(arr1)  # arr = n * n

    # 도착지점 찾기
    new_list = []
    for j in range(n):
        if arr1[99][j] == 1:
            start1 = [99, j]
            new_list.append(list(count_ladder(arr1, start1)))

    min1 = new_list[0][0]
    for i in range(len(new_list)):
        if new_list[i][0] <= min1:
            min1 = new_list[i][0]
            answer = new_list[i][1]

    print(f'#{tc} {answer}')


