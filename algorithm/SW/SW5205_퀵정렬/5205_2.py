import sys
sys.stdin = open('sample_input.txt')


def lomuto(arr, p, r):
    x = arr[r]  # 맨 오른쪽 원소
    i = p - 1

    # i와 j가 한 방향으로 이동
    for j in range(p, r):
        # i는 피봇보다 작은 값을 만나야 이동
        if arr[j] <= x:
            i += 1
            # 피봇 보다 큰 값이 시작하는 위치와 교환
            arr[i], arr[j] = arr[j], arr[i]
    # j가 끝까지 도착하게 되면 i+1부터 j까지 피봇보다 큰 값
    # i+1과 피봇값 교환
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1


def quickSort(arr, l, r):
    if l < r:
        s = lomuto(arr, l, r)
        # 피봇 값을 중심으로 다시 왼쪽과 오른쪽 실행
        quickSort(arr, l, s - 1)
        quickSort(arr, s + 1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    quickSort(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')