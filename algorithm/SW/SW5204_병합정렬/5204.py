import sys
sys.stdin = open('sample_input.txt')


def merge_sort(arr):
    global count
    # 기본 파트
    if len(arr) == 1:
        return arr
    # 유도 파트
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    l_len = len(left)
    r_len = len(right)
    idx = l_idx = r_idx = 0
    while l_idx < l_len and r_idx < r_len:
        if left[l_idx] <= right[r_idx]:
            arr[idx] = left[l_idx]
            l_idx += 1
        else:
            arr[idx] = right[r_idx]
            r_idx += 1
        idx += 1

    if r_idx == r_len:
        count += 1
        for i in range(l_idx, l_len):
            arr[idx] = left[i]
            idx += 1
    elif l_idx == l_len:
        for i in range(r_idx, r_len):
            arr[idx] = right[i]
            idx += 1
    return arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {count}')