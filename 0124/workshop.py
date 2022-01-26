# 1
# def get_dict_avg(scores):
#     count = 0
#     total = 0
#     for score in scores.values():
#         count += 1
#         total += score
#     scores_avg = total / count
#     return scores_avg

# print(get_dict_avg({'python': 80, 'algorithm': 90, 'django': 89, 'web': 83}))



# 2
def count_blood(blood):
    my_count = {}
    for key in blood:
        my_count[key] = blood.count(key)
    return my_count
        
print(count_blood([
	'A', 'B', 'A', 'O', 'AB', 'AB',
	'O', 'A', 'B', 'O', 'B', 'AB',
])) #=> {'A':3, 'B':3, 'O':3, 'AB':3}