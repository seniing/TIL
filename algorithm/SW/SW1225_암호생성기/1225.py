import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    while arr[7] != 0:
        for j in range(1, 6):
            a = arr[0] - j
            if a > 0:
                arr.append(a)
                arr.pop(0)
            else:
                arr.append(0)
                arr.pop(0)
                print(f'#{tc}', *arr)
                break
