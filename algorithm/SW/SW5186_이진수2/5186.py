import sys
sys.stdin = open('sample_input.txt')


# 2진수 만들기
def binary(num):
    result = ''
    for i in range(12):
        if num - 0.5**(i+1) >= 0:
            result += '1'
            num = num - 0.5**(i+1)
        else:
            result += '0'
        # 더이상 뺄 숫자가 없으면 이진수 완성
        if num == 0:
            return result
    # 13자리 이상이 필요한 경우 'overflow' 출력
    if num != 0:
        return 'overflow'


T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {binary(N)}')