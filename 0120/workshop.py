# 1
import numbers


def get_secret_word(lst):
    word = '' # word 초기화
    for i in lst: 
        word += chr(i) # 정수에 대응되는 아스키 문자를 변환해 word에 저장
    return word

print(get_secret_word([83, 115, 65, 102, 89]))

#2
def get_secret_number(word):
    number = 0 # number 초기화
    for i in word:
        number += ord(i) # 문자에 대응되는 아스키 숫자를 변환에 number에 저장
    return number

print(get_secret_number('tom'))

#3
def get_strong_word(word1, word2):
    num_1 = 0 # word1의 아스키 숫자 합
    num_2 = 0 # word2의 아스키 숫자 합
    for i in word1:
        num_1 += ord(i) # word1 문자에 대응되는 아스키 숫자를 변환에 num_1에 저장
    for j in word2:
        num_2 += ord(j) # word2 문자에 대응되는 아스키 숫자를 변환에 num_2에 저장
    if num_1 > num_2: # num1이 num2보다 크면
        return word1 # word1 반환
    else:
        return word2

print(get_strong_word('z', 'a')) #=> 'z'
print(get_strong_word('tom', 'john')) #=> 'john'