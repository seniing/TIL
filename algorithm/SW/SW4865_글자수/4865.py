import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str_dic = {}

    # str1 안의 문자들로 dictionary 생성
    for i in str1:
        str_dic[i] = 0
    # str2 안에 str_dic key 값과 같은 것이 있으면 1씩 더해준다
    for i in str2:
        for j in str_dic:
            if i == j:
                str_dic[j] += 1
    # max 값 찾기
    str_max = 0
    for i in str_dic.values():
        if i > str_max:
            str_max = i

    print(f'#{tc} {str_max}')







