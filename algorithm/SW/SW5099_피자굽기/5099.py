import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    fire = []
    num = 1

    for i in range(N):
        fire.append([pizza.pop(0), num])
        num += 1

    while len(fire) > 1:
        p, i = fire.pop(0)
        p //= 2
        if p == 0:
            if pizza:
                fire.append([pizza.pop(0), num])
                num += 1
        else:
            fire.append([p, i])

    print(f'#{tc} {fire[0][1]}')
