import sys
sys.stdin = open('sample_input.txt')


def partition(arr, l, r):
    p = arr[l]  # 피봇 값(처음)
    i = l       # 왼쪽에서 시작
    j = r       # 오른쪽에서 시작
    while i <= j:
        # 피봇 값 보다 큰 값을 만나면 종료
        while i <= j and arr[i] <= p:
            i += 1
        # 피봇 값 보다 작은 값을 만나면 종료
        while i <= j and arr[j] >= p:
            j -= 1
        # i와 j가 서로 교차되지 않았다면 큰 값과 작은 값 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    # i와 j가 교차할 때 피봇 값과 작은 값 교환
    # 피봇을 기준으로 왼쪽은 피봇보다 작은 값들만 위치 오른쪽은 피봇보다 큰 값들만 위치
    arr[l], arr[j] = arr[j], arr[l]
    # 피봇값의 index
    return j


def quickSort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        # 피봇 값을 중심으로 다시 왼쪽과 오른쪽 실행
        quickSort(arr, l, s - 1)
        quickSort(arr, s + 1, r)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, len(arr)-1)

    print(f'#{tc} {arr[N//2]}')