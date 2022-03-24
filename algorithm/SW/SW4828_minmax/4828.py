import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # len(arr)
    arr = list(map(int, input().split()))

    max_arr = arr[0]
    min_arr = arr[0]
    for i in arr:
        if i > max_arr:
            max_arr = i
        elif i < min_arr:
            min_arr = i

    print(f'#{tc} {max_arr - min_arr}')
