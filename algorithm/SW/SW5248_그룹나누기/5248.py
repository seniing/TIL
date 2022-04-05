import sys
sys.stdin = open('sample_input.txt')


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    rep = [i for i in range(N+1)]

    arr = list(map(int, input().split()))
    for i in range(M):
        a = arr[i*2]
        b = arr[i*2 + 1]
        union(a, b)

    answer = set()
    for i in rep:
        answer.add(find_set(i))

    print(f'#{tc} {len(answer)-1}')
