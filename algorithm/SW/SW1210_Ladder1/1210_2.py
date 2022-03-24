import sys
sys.stdin = open('input.txt')

for _ in range(10):
    N = input()
    matrix = [list(map(int, input().split())) for _ in range(100)]  # 2차원 사다리 배열

    r = 99
    for i in range(100):
        if matrix[99][i] == 2:  # 도착 지점의 열 번호 찾기
            c = i
            break

    d = [-1, 1]  # 좌우 만 확인하기

    while r > 0:  # row = 0 : 도착점
        for i in range(2):
            nc = c + d[i]

            if 0 <= nc < 100 and matrix[r][nc]:  # 사다리 판을 벗어나지 않으면서 좌우로 이동 가능한지 여부를 확인
                matrix[r][c] = 0  # 행 방향 이동 전 사다리 상태를 위치를 0으로 변경
                c = nc            # 행 방향 이동
                break
        else:
            r -= 1                # 열 방향 이동

    print(f'#{N} {c}')