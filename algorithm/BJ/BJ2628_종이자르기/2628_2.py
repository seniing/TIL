
x_line = [7, 6, 5, 4, 3, 2, 1]

# 오름차순 정렬
for i in range(len(x_line) - 1):
    min_i = i
    for j in range(i+1, len(x_line)):
        if x_line[min_i] > x_line[j]:
            min_i = j
        x_line[i], x_line[min_i] = x_line[min_i], x_line[i]
print(x_line)




