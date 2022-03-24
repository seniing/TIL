import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    a = list(map(str, input()))
    arr = []
    for i in a:
        # 여는 괄호가 나오면 추가
        if i == '(' or i == '{':
            arr.append(i)
        # 닫는 괄호가 나왔을 때 top 값과 짝을 이루면 그 값 삭제
        elif i == ')':
            if arr and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(i)
        elif i == '}':
            if arr and arr[-1] == '{':
                arr.pop()
            else:
                arr.append(i)

    # 아무것도 없으면 정상적으로 짝을 이룬 경우
    if len(arr) == 0:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')
