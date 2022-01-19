#1
# N = int(input('N은 1이상 1,000이하의 정수이다. (1 =< N =< 1.000): '))

#1-1
# for i in range(1, N+1):
#     if N % i == 0:
#         print(i, end = ' ')

#1-2
# result = []
# for i in range(1, N+1):
#      if N % i == 0:
#          result += [i]
# print(*result)


#2
numbers = [
	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

n = len(numbers)
for i in range(0, n-1):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

median = 0
if n % 2 == 0:
    median1 = n//2 - 1
    median2 = n//2
    print((int(numbers[median1]) + int(numbers[median2])) / 2)
else:
    median = n//2 + 1
    print(numbers[median])


#3
# N = int(input())
# n = []

# for i in range(1, N + 1):
#     n += [i]
#     print(*n)