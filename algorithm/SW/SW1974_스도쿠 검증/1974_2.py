import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = 1

    # 행과 열 검사
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[i][j]] += 1
            if cnt[arr[i][j]] == 2:
                ans = 0
        #         break
        # if ans == 0:
        #     break
    for i in range(9):
        cnt = [0] * 10
        for j in range(9):
            cnt[arr[j][i]] += 1
            if cnt[arr[i][j]] == 2:
                ans = 0
        #         break
        # if ans == 0:
        #     break

    # 3*3 영역 검사
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            cnt = [0] * 10
            for k in range(3):
                for l in range(3):
                    cnt[arr[i+k][j+l]] += 1
                    if cnt[arr[i+k][j+l]] == 2:
                        ans = 0
                        # break

    print(f'#{tc} {ans}')