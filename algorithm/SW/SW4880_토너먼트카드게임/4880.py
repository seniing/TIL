import sys
sys.stdin = open('sample_input.txt')


def winner(a, b):
    if arr[a-1] - arr[b-1] == -1 or arr[a-1] - arr[b-1] == 2:
        return b
    else:
        return a


def vs(start, end):
    if start == end:
        return start

    left, right = vs(start, (start+end)//2), vs((start+end)//2+1, end)
    return winner(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {vs(1, N)}')