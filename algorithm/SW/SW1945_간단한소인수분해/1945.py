import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = [2, 3, 5, 7, 11]
    answer = ''

    for i in num:
        count = 0
        while N % i == 0:
            N = N//i
            count += 1
        answer += str(count)
    answer_print = ' '.join(answer)
    print(f'#{tc} {answer_print}')
