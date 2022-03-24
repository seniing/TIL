import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 수열의 길이
    arr = []  # 수열
    for i in input():
        arr.append(int(i))

    count = 0
    answer = 0
    for i in arr:
        if i == 1:
            count += 1
            if count > answer:
                answer = count
        else:
            count = 0

    # arr_str = input()
    # count = 0
    # answer = 0
    # for i in arr_str:
    #     if int(i) == 1:
    #         count += 1
    #         if count > answer:
    #             answer = count
    #     else:
    #         count = 0

    print(f'#{tc} {answer}')