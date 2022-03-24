import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    arr = []
    for i in text:
        if not arr or arr[-1] != i:
            arr.append(i)
        else:
            arr.pop()
    print(f'#{tc} {len(arr)}')