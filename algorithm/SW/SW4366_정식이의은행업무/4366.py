import sys
sys.stdin = open('sample_input.txt')


def TWO(n):
    n = n[::-1]
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * 2**i
    return result


def THREE(n):
    n = n[::-1]
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * 3**i
    return result


T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()
    two_list = []
    three_list = []

    for i in range(len(two)):
        a = list(two)
        if a[i] == '0':
            a[i] = '1'
        else:
            a[i] = '0'
        two_list.append(TWO(a))

    for i in range(len(three)):
        a = list(three)
        if a[i] == '0':
            a[i] = '1'
            three_list.append(THREE(a))
            a[i] = '2'
            three_list.append(THREE(a))
        elif a[i] == '1':
            a[i] = '0'
            three_list.append(THREE(a))
            a[i] = '2'
            three_list.append(THREE(a))
        else:
            a[i] = '0'
            three_list.append(THREE(a))
            a[i] = '1'
            three_list.append(THREE(a))

    for i in two_list:
        for j in three_list:
            if i == j:
                print(f'#{tc} {i}')