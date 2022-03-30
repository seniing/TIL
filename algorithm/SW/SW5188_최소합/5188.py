import sys
sys.stdin = open('sample_input.txt')

dx = [0, 1]
dy = [1, 0]
def dfs(x, y, total):
    global answer
    total += arr[x][y]
    if total > answer:
        return
    if x == N - 1 and y == N - 1:
        if answer > total:
            answer = total
            return
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            dfs(nx, ny, total)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 999999999
    dfs(0, 0, 0)
    print(f'#{tc} {answer}')
