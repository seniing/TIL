# 1
# def list_sum(lst):
#     total = 0
#     for i in lst:
#         total += i
#     return total

# print(list_sum([1, 2, 3, 4, 5])) #=> 15



# 2
# def dict_list_sum(dict):
#     total = 0
#     for i in dict:
#         for j in i:
#             if 'age' == j:
#                 total += i[j]
#     return total

# def dict_list_sum(dict):
#     total = 0
#     for i in dict:
#         total += i['age']
#     return total

# dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]) #=> 16
# print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])) #=> 16


# 3
# def all_list_sum(lst):
#     total = 0
#     for i in lst:
#         for j in i:
#             total += j
#     return total

# all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
# print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])) #=> 55