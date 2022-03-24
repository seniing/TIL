import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 칠할 영역의 개수
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                matrix[j][k] += color
                if matrix[j][k] == 3:
                    cnt += 1
    print(f'#{tc} {cnt}')