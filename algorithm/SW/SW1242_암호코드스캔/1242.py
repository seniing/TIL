import sys
sys.stdin = open('sample_input.txt')

# 16진수
hex = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

scode = {
    211: 0,
    221: 1,
    122: 2,
    411: 3,
    132: 4,
    231: 5,
    114: 6,
    312: 7,
    213: 8,
    112: 9
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = ['' for _ in range(N)]

    # 16진수를 2진수로 변환하기
    for i in range(N):
        temp = input()
        for j in range(M):
            arr[i] += hex[temp[j]]

    answer = 0
    for i in range(N):
        # 뒤쪽 인덱스부터 탐색
        j = M*4 -1
        # j가 56보다 작으면 암호 코드가 아니다
        while j >= 55:
            if arr[i][j] == '1' and arr[i-1][j] == '0':
                # 1 : 0 : 1 의 비율 구하기
                code = [0] * 8
                for k in range(7, -1, -1):
                    a = b = c = 0
                    while arr[i][j] == '1':
                        c += 1
                        j -= 1
                    while arr[i][j] == '0':
                        b += 1
                        j -= 1
                    while arr[i][j] == '1':
                        a += 1
                        j -= 1
                    while arr[i][j] == '0':
                        j -= 1
                    # 비율 찾기
                    d = min(a, b, c)
                    a //= d
                    b //= d
                    c //= d
                    # 코드 찾기
                    code[k] = scode[100*a+10*b+c]

                # 검증코드가 맞는지 살펴보기
                odd = 0
                even = 0
                for k in range(8):
                    if k % 2:
                        even += code[k]
                    else:
                        odd += code[k]
                if (odd * 3 + even) % 10 == 0:
                    answer += odd + even
                # 코드 검증이 끝나면 index 값 한칸 뒤로
                j += 1
            j -= 1

    print(f'#{tc} {answer}')