import sys
sys.stdin = open('sample_input.txt')


def check(x, y):
    global answer

    for i in range(5):
        count = 0
        for j in range(5):
            if arr[x+i][y+j] == 'o':
                count += 1
        if count == 5:
            answer = 'YES'

    for i in range(5):
        count = 0
        for j in range(5):
            if arr[x+j][y+i] == 'o':
                count += 1
        if count == 5:
            answer = 'YES'

    count = 0
    for i in range(5):
        if arr[x+i][y+i] == 'o':
            count += 1
    if count == 5:
        answer = 'YES'

    count = 0
    for i in range(5):
        if arr[x+i][y+4-i] == 'o':
            count += 1
    if count == 5:
        answer = 'YES'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    answer = 'NO'

    for x in range(N-4):
        for y in range(N-4):
            check(x, y)
    print(f'#{tc} {answer}')
