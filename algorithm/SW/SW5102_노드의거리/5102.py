import sys
sys.stdin = open('sample_input.txt')


def bfs(S, G, arr):
    queue = [S]
    visited = [0] * (V+1)
    answer = 0
    while queue:
        a = queue.pop(0)
        for i in arr[a]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[a] + 1
                answer = visited[i]
            if i == G:
                return answer
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G, arr)}')