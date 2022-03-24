import sys
sys.stdin = open('sample_input.txt')


def search_M(text):
    M = len(text)  # text 의 길이
    # JAEZNNZEAJ -> [0],[M-1] / [1],[M-2] / ...
    # M//2 전 까지만 반복
    for i in range(M//2):
        if text[i] != text[M-1-i]:
            return 0             # 만약 다른 값이면 0 출력
            break
    else:
        return text              # 모두 같은 값이면 text 출력


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # n * n 배열, 회문의 길이
    arr = [list(map(str, input())) for _ in range(N)]

    for i in range(N):  # 기준
        for j in range(N-M+1):  # 회문의 길이를 생각해서 반복
            row = ''
            column = ''
            for k in range(j, j+M):  # 회문의 길이 만큼 반복
                row += arr[i][k]  # 행 우선 순회
                column += arr[k][i]  # 열 우선 순회
            if search_M(row) != 0:
                print(f'#{tc} {search_M(row)}')
            elif search_M(column) != 0:
                print(f'#{tc} {search_M(column)}')



