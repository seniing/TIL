import sys
sys.stdin = open('input.txt')

def maxlength_M(arr):
    max_M = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:            # list 안에서 같은 값이 있으면
                text = ''.join(arr[i:j+1])  # i 번째에서 j 번째 까지만 : list -> str
                M = len(text)               # text 의 길이
                if text == text[::-1]:      # text 를 뒤집은 것과 같다면 회문
                    # 회문 길이의 max 값 찾기
                    if M > max_M:
                        max_M = M
    return max_M


T = 10
for tc in range(1, T+1):
    n = input()
    row_arr = [list(map(str, input())) for _ in range(100)]
    len_arr = len(row_arr)

    col_arr = []
    for i in range(len_arr):
        a = [row_arr[j][i] for j in range(len_arr)]
        col_arr.append(a)

    len_max = 0
    # 열 순회
    for i in row_arr:
        if maxlength_M(i) > len_max:
            len_max = maxlength_M(i)
    # 행 순회
    for i in col_arr:
        if maxlength_M(i) > len_max:
            len_max = maxlength_M(i)

    print(f'#{tc} {len_max}')