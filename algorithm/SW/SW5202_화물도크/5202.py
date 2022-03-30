import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    truck = []

    for i in arr:
       truck.append([i[1] - i[0], i[0], i[1]])
    truck = sorted(truck)

    time = [0] * 25
    count = 0
    for i in truck:
        if 1 not in time[i[1]:i[2]]:
            count += 1
            for j in range(i[1], i[2]):
                if time[j] == 0:
                    time[j] = 1
    print(f'#{tc} {count}')