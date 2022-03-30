import sys
sys.stdin = open('sample_input.txt')


def check(arr, n):
    for i in range(n-2):
        if arr[i] + 1 in arr and arr[i] + 2 in arr:
            return True
        elif arr[i] == arr[i+1] == arr[i+2]:
            return True
    return False


T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))

    p1 = []
    p2 = []
    answer = 0
    for i in range(0, 12, 2):
        p1.append(card[i])
        p2.append(card[i+1])

        if i >= 4:
            if check(sorted(p1), i//2+1):
                answer = 1
                break

            if check(sorted(p2), i//2+1):
                answer = 2
                break

    print(f'#{tc} {answer}')
