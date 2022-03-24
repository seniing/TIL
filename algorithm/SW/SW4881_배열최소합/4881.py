import sys
sys.stdin = open('sample_input.txt')


def arr_sum(idx, a):
    global min_sum
    if a > min_sum:
        return
    if idx == N:
        if a < min_sum:
            min_sum = a

    for i in range(N):
        if not use[i]:
            use[i] = 1
            arr_sum(idx+1, a+arr[idx][i])
            use[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    use = [0] * N
    min_sum = 100

    arr_sum(0, 0)
    print(f'#{tc} {min_sum}')