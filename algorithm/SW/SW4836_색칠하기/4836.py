import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 칠할 영역의 개수
    red_lst = []  # [[2, 2, 4, 4]]
    blue_lst = []  # [[3, 3, 6, 6]]
    for i in range(N):
        lst = list(map(int, input().split()))
        if lst[-1] == 1:  # 마지막 숫자 = 1 = 빨강
            red_lst.append(lst[:-1])  # 마지막 숫자를 제외하고 red_lst 에 추가
        else:
            blue_lst.append(lst[:-1])  # 마지막 숫자를 제외하고 blue_lst 에 추가

    red = []  # [22, 23, 24, 32, 33, 34, 42, 43, 44]
    blue = []  # [33, 34, 35, 36, 43, 44, 45, 46, 53, 54, 55, 56, 63, 64, 65, 66]
    for i in red_lst:
        for j in range(i[0], i[2]+1):  # [0]번째 값과 [2] 번째 값이 row
            for k in range(i[1], i[3]+1):  # [1]번째 값과 [3] 번째 값이 column
                red.append(j*10+k)

    for i in blue_lst:
        for j in range(i[0], i[2]+1):  # [0]번째 값과 [2] 번째 값이 row
            for k in range(i[1], i[3]+1):  # [1]번째 값과 [3] 번째 값이 column
                blue.append(j*10+k)

    answer = 0
    for i in red:
        for j in blue:
            if i == j:  # red 와 blue 중 같은 값이 있으면 보라색!
                answer += 1
    print(f'#{tc} {answer}')