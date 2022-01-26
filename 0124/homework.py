# 1
def count_vowels(word):
    word_count = 0
    my_list = ['a', 'e', 'i', 'o', 'u']
    for i in my_list:
        word_count += word.count(i)
    return word_count

print(count_vowels('apple')) #=> 2
print(count_vowels('banana')) #=> 3



# 2
def only_square_area(list_1, list_2):
    square_area = []
    for i in list_1:
        for j in list_2:
            if i == j:
                square_area.append(i * j)
    return square_area

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
#=> [1024, 3025]