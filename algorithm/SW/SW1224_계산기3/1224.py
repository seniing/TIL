import sys
sys.stdin = open('input.txt')


def make_expression(a):
    isp = {')': 0, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
    icp = {')': 0, '*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    stack = []
    ans = ''
    for i in a:
        # 숫자일 때는 출력
        if i in num:
            ans += i
        # 닫는 괄호를 만났을때, 스택이 비어있지 않고 여는 괄호가 아니면 연산자 출력
        # 여는 괄호를 만났을 때는 여는 괄호 버리기
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        # 들어갈 연산자가 stack 의 top 에 있는 연산자보다 값이 적다면 연산자를 출력
        # 안에 있는 연산자보다 값이 커졌을 땐 stack 에 연산자 추가
        else:
            while stack and icp[i] <= isp[stack[-1]]:
                ans += stack.pop()
            stack.append(i)
    # stack 이 비어있을 때까지 연산자 출력
    while stack:
        ans += stack.pop()
    return ans


def calculation(a):
    n = len(a)
    stack = []
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for i in a:
        if i in num:
            stack.append(int(i))
        else:
            if i == '*':
                x = stack.pop() * stack.pop()
                stack.append(x)
            elif i == '+':
                x = stack.pop() + stack.pop()
                stack.append(x)
    return stack[0]


T = 10
for tc in range(1, T+1):
    N = int(input())
    a = input()
    print(f'#{tc} {calculation(make_expression(a))}')