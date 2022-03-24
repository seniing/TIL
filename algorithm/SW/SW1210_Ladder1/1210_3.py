import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = input()
    arr = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]  # 2차원 사다리 배열

    s = 0
    for j in range(1, 101):
        if arr[99][j] == 2:
            s = j
            break

    # 도착에서 반대로 시작
    i = 99
    while i > 0:
        if arr[i][s-1] == 1:
            arr[i][s] = 0
            s -= 1
        elif arr[i][s+1] == 1:
            arr[i][s] = 0
            s += 1
        else:
            i -= 1
    print(f'#{tc} {s-1}')
