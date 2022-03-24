import sys
sys.stdin = open('sample_input.txt')


def Forth():
    stack = []
    for i in arr:
        if i.isdigit():
            stack.append(int(i))
        elif len(stack) > 1:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(a // b)
            else:
                return 'error'
        elif stack and i == '.':
            return stack[0]
        else:
            return 'error'


T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    print(f'#{tc} {Forth()}')
