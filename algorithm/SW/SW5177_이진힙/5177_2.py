import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] + list(map(int, input().split()))
    answer = 0

    for i in range(1, N+1):
        p = i // 2
        c = i
        while p >= 1 and tree[p] > tree[c]:
            tree[p], tree[c] = tree[c], tree[p]
            c = p
            p = c // 2

    a = N // 2
    while a > 0:
        answer += tree[a]
        a //= 2
    print(f'#{tc} {answer}')


