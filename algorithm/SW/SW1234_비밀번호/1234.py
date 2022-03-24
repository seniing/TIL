import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, text = map(str, input().split())
    arr = []
    for i in text:
        if arr and i == arr[-1]:  # arr 안에 값이 있고, 맨 마지막 값이 i와 같다면 마지막 값 삭제
            arr.pop()
        else:                     # 그렇지 않다면 i 추가
            arr.append(i)

    answer = ''.join(map(str, arr))
    print(f'#{tc} {answer}')