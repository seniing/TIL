# 1
# def duplicated_letters(word):
#     result = []
#     for i in set(word):
#         if word.count(i) > 1:
#             result.append(i)
#     return result

# print(duplicated_letters('apple')) #=> ['p']
# print(duplicated_letters('banana')) #=> ['a', 'n']



# 2
# def low_and_up(word):
#     new_word = ''
#     for i in range(len(word)):
#         if i % 2:
#             new_word += word[i].upper()
#         else:
#             new_word += word[i].lower()
#     return new_word

# print(low_and_up('apple')) #=> aPpLe
# print(low_and_up('banana')) #=> bAnAnA



# 3
def lonely(lst):
    new_lst = []
    for i in range(len(lst)):
        if i == 0:
            new_lst.append(lst[i])
        elif lst[i] == lst[i-1]:
            pass
        else:
            new_lst.append(lst[i])
    return new_lst

print(lonely([1, 1, 3, 3, 0, 1, 1])) #=> [1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) #=> [4, 3]
