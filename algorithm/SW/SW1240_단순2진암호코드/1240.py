import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 0 ~ 9 까지의 코드
    num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    # 코드는 1을 포함하기 때문에 1을 포함하는 줄 찾기
    C = ''
    for i in range(N):
        a = input()
        if '1' in a:
            C = a

    # 암호는 끝이 1로 끝나고 총 56개
    code_2 = C[::-1]
    while True:
        if code_2[0] == '0':    # 0은 삭제
            code_2 = code_2[1:]
        elif code_2[0] == '1':  # 1을 만나면 끝나기
            break
    code_2 = code_2[:56]        # 뒤에서부터 1을 시작으로 56개만 저장
    code = code_2[::-1]         # 다시 뒤집기

    # 7개씩 보며 암호 찾기
    arr = []
    for i in range(0, 56, 7):
        # num 안에 같은 값이 있으면 그 값의 index 가 암호
        for j in range(len(num)):
            if code[i:i+7] == num[j]:
                arr.append(j)

    odd = 0
    even = 0
    for k in range(8):
        if k % 2:
            even += arr[k]
        else:
            odd += arr[k]
    if (odd * 3 + even) % 10 == 0:
        answer = odd + even
    else:
        answer = 0
    print(f'#{tc} {answer}')
