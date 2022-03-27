import sys
sys.stdin = open('sample_input.txt')


def start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return [i, j]


def bfs(n, arr):
    queue = [n]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == '0':
                    arr[nx][ny] = int(arr[x][y]) + 1
                    queue.append([nx, ny])
                elif arr[nx][ny] == '3':
                    return arr[x][y]-2
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    s = start(arr)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    print(f'#{tc} {bfs(s, arr)}')
