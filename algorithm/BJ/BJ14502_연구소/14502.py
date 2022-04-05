# pypy 통과

def dfs():
    global max_result
    copy = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy[i][j] = arr[i][j]

    result = 0
    stack = []
    for i in range(N):
        for j in range(M):
            if copy[i][j] == 2:
                stack.append((i, j))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    while stack:
        x, y = stack.pop()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    stack.append((nx, ny))

    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    if result > max_result:
        max_result = result


def wall(count):
    if count == 3:
        dfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(count+1)
                arr[i][j] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_result = 0

wall(0)
print(max_result)
