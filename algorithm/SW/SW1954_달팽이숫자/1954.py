import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N_list = [[0]*N for _ in range(N)]

    num = 1
    x1 = 0
    y1 = 0
    n = N

    while n > 1:
        for i in range(n-1):
            N_list[x1][y1] = num
            num += 1
            y1 += 1

        for i in range(n-1):
            N_list[x1][y1] = num
            num += 1
            x1 += 1

        for i in range(n-1):
            N_list[x1][y1] = num
            num += 1
            y1 -= 1

        for i in range(n-1):
            N_list[x1][y1] = num
            num += 1
            x1 -= 1

        x1 += 1
        y1 += 1
        n -= 2

    if n == 1:  # n이 홀수일때는 정 가운데 값 하나에 마지막 값이 들어간다
        N_list[N//2][N//2] = num

    print(f'#{tc}')
    for i in N_list:
        answer = ''
        answer += ' '.join(map(str, i))
        print(answer)















