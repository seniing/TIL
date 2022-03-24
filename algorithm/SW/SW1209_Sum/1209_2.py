import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # 행의 합
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[i][j]
        if s > max_sum:
            max_sum = s
    # 열의 합
    for i in range(100):
        s = 0
        for j in range(100):
            s += arr[j][i]
        if s > max_sum:
            max_sum = s
    # 오른쪽 아래 대각선의 합
    s = 0
    for i in range(100):
        s += arr[i][i]
    if s > max_sum:
        max_sum = s
    # 왼쪽 아래 대각선의 합
    s = 0
    for i in range(100):
        s += arr[i][99-i]
    if s > max_sum:
        max_sum = s

    print(f'#{tc} {max_sum}')

