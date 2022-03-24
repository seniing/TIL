import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(16)]

    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                x, y = i, j

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    stack = [(x, y)]
    answer = 0
    while stack:
        x1, y1 = stack.pop()
        for k in range(4):
            nx = x1 + dx[k]
            ny = y1 + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16:
                if arr[nx][ny] == '0':
                    stack.append((nx, ny))
                    arr[nx][ny] = '2'
                elif arr[nx][ny] == '3':
                    answer = 1
                    break

    print(f'#{tc} {answer}')
