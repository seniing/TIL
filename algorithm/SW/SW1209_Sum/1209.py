import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    n = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_list = []
    # 각 행의 합
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        max_list.append(sum_row)
    # 각 열의 합
    for j in range(100):
        sum_col = 0
        for i in range(100):
            sum_col += arr[i][j]
        max_list.append(sum_col)
    # 대각선의 합
    sum_dia1 = 0
    sum_dia2 = 0
    for i in range(100):
        sum_dia1 += arr[i][i]
        sum_dia2 += arr[i][99-i]
    max_list.append(sum_dia1)
    max_list.append(sum_dia2)

    # 최대값 구하기
    answer = max_list[0]
    for m in max_list:
        if m > answer:
            answer = m

    print(f'#{n} {answer}')

