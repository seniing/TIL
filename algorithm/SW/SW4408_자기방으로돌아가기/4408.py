import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ready = [list(map(int, input().split())) for _ in range(N)]
    corridor = [0] * 201
    cnt = 0

    for r in ready:
        if r[0] > r[1]:
            r[0], r[1] = r[1], r[0]
        s, e = (r[0]+1)//2, (r[1]+1)//2
        for i in range(s, e+1):
            corridor[i] += 1

    for j in corridor:
        if cnt < j:
            cnt = j

    print(f'#{tc} {cnt}')