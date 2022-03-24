import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())  # len(arr)
    arr = list(map(int, input().split()))

    count = 0
    for i in range(2, N-2):
        # i번째 빌딩을 기준으로 왼쪽 2개 빌딩 오른쪽 2개의 빌딩 list
        i_list = arr[i-2:i+3]

        # list 최댓값 구하기
        max_list = 0
        for j in range(5):
            if j != 2:  # 기준이 되는 빌딩 제외
                if i_list[j] > max_list:
                    max_list = i_list[j]

        # 기준이 되는 빌딩이 왼쪽 2개와 오른쪽 2개의 빌딩 보다 높다면
        if arr[i] > max_list:
            # 빌딩의 높이 - list 중 가장 높은 빌딩 = 조망권이 확보된 세대의 수
            count += arr[i] - max_list

    print(f'#{tc} {count}')
