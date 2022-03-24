import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 수열의 길이
    arr = list(map(int, input().split()))  # 수열

    count = 1
    answer = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1] + 1:
            count += 1
            if count > answer:
                answer = count
        else:
            count = 1

    print(f'#{tc} {answer}')