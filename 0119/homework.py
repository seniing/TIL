#2
# def get_middle_char(word):
#     length = len(word)
#     if length % 2:
#         return print(word[length // 2])
#     else:
#         return print(word[length // 2 - 1 :  length // 2 + 1])

# get_middle_char('ssafy') #=>a
# get_middle_char('coding') #=> di



#3
# def ssafy(name, location='서울'):
# 	print(f'{name}의 지역은 {location}입니다.')
	
# #(1)
# ssafy('허준')
# #(2)
# ssafy(location='대전', name='철수')
# #(3)
# ssafy('영희', location='광주')
# #(4)
# # ssafy(name='길동', '구미')



#4
# def my_func(a, b):
# 	c = a + b
# 	print(c)
	
# result = my_func(3, 7)
# print(result)



#5
# def my_avg(*numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     avg = total / len(numbers)
#     return print(avg)


# my_avg(77, 83, 95, 80, 70) #=> 81.0