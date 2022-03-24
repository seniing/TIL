import sys
sys.stdin = open('input.txt')

def search_round(arr):
    answer = 0
    for i in range(len(arr)-n+1):
        text = ''.join(arr[i:i+n])  # i 번째 부터 n개 까지만
        if text == text[::-1]:      # text 를 뒤집은 것과 같다면 회문
            answer += 1
    return answer


T = 10
for tc in range(1, T+1):
    n = int(input())
    row_arr = [list(map(str, input())) for _ in range(8)]
    len_arr = len(row_arr)

    col_arr = []
    for i in range(len_arr):
        a = [row_arr[j][i] for j in range(len_arr)]
        col_arr.append(a)

    # 열 순회
    answer = 0
    for i in row_arr:
        answer += search_round(i)
    # 행 순회
    for i in col_arr:
        answer += search_round(i)

    print(f'#{tc} {answer}')