def nCr(n, r, s):
    global min_result
    if r == 0:
        result = 0
        for i in home:
            a = 100
            for j in comb:
                distance = abs(i[0] - j[0]) + abs(i[1] - j[1])
                if distance < a:
                    a = distance
            result += a
        if result < min_result:
            min_result = result
    else:
        for i in range(s, n-r+1):
            comb[len(comb)-r] = chicken[i]
            nCr(n, r-1, i+1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])
        elif arr[i][j] == 1:
            home.append([i, j])

comb = [[] for _ in range(M)]
min_result = 10000

nCr(len(chicken), M, 0)

print(min_result)
