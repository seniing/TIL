import sys
sys.stdin = open('sample_input.txt')

# 16진수
arr = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
# 2진수 만들기
def binary(num):
    result = ''
    for i in range(4):
        result += str(num % 2)
        num = num // 2
    return result[::-1]


T = int(input())
for tc in range(1, T+1):
    N, H = map(str, input().split())

    answer = ''
    for s in H:
        answer += binary(arr[s])
    print(f'#{tc} {answer}')
