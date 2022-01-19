#2
# odd_num = [i for i in range(1,51) if i % 2 ==1]

# odd_num = list(range(1, 51, 2))
# print(odd_num)

# 3
# students = {'박세은' : 25}

#4
# n = 5
# m = 9
# s = ''

# for i in range(0,n):
#     s += '*'
# for i in range(0,m):
#     print(s)

#5
# temp = 36.5
# if temp >= 37.5:
# 	print('입실 불가')
# else:
# 	print('입실 가능')

# status = '입실 불가' if temp >= 37.5 else '입실 가능'
# print(status)

#6
scores = [80, 89, 99, 83]
n = 0
total = 0

for i in scores:
    total +=i
    n += 1

avg = total/n
print(avg)