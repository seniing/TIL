import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N = 정수의 개수
    # M = 구간의 개수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # N -> 10, M -> 3 : 계산 끝 [7] = N-M
    cal_list = []
    for i in range(N-M+1):
        cal = 0
        for j in range(i, i+M):
            cal += arr[j]
        cal_list.append(cal)

    # 가장 큰 값 구하기
    cal_max = cal_list[0]
    cal_min = cal_list[0]
    for cal in cal_list:
        if cal > cal_max:
            cal_max = cal
        elif cal < cal_min:
            cal_min = cal

    print(f'#{tc} {cal_max - cal_min}')