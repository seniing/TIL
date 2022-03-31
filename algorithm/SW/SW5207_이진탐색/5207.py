import sys
sys.stdin = open('sample_input.txt')


def search(arr, a, position):
    global count

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if a == arr[mid]:
            count += 1
            return
        elif a < arr[mid]:
            if position == 'r':
                return
            end = mid - 1
            position = 'r'
        else:
            if position == 'l':
                return
            start = mid + 1
            position = 'l'
    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    n = sorted(n)
    m = list(map(int, input().split()))
    count = 0
    position = ''

    for i in m:
        search(n, i, position)

    print(f'#{tc} {count}')