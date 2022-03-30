def result(count, total, a, b, c, d):
    global max_answer, min_answer
    if count == N:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return
    if a:
        result(count+1, total + arr[count], a-1, b, c, d)
    if b:
        result(count+1, total - arr[count], a, b-1, c, d)
    if c:
        result(count+1, total * arr[count], a, b, c-1, d)
    if d:
        result(count+1, total // arr[count] if total >= 0 else -(-total // arr[count]), a, b, c, d-1)


N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_answer = -1000000000
min_answer = 1000000000
result(1, arr[0], operator[0], operator[1], operator[2], operator[3])
print(max_answer)
print(min_answer)

