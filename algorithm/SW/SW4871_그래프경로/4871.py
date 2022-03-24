import sys
sys.stdin = open('sample_input.txt')


def dfs(s, g):
    stack = [s]
    while stack:
        s = stack.pop()
        if s == g:
            return 1
        if visited[s] == 0:
            visited[s] = 1
            for v in range(1, V+1):
                if arr[s][v] == 1 and visited[v] == 0:
                    stack.append(v)
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1

    S, G = map(int, input().split())

    visited = [0] * (V+1)
    print(f'#{tc} {dfs(S, G)}')
