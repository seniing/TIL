import sys
sys.stdin = open('sample_input.txt')


def dfs():
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    stack.append((nx, ny))
                    arr[nx][ny] = 1
                elif arr[nx][ny] == 3:
                    return 1
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    stack = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                stack.append((i, j))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    print(f'#{tc} {dfs()}')