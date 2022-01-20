#3
#재귀함수
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))

#반복문
def fib_loop(n):
    if n < 2:
        return n
    lst = [0, 1]
    for i in range(2, n+1):
        lst.append(lst[i-1] + lst[i-2])
    return lst[-1]

print(fib_loop(10))

#재귀함수 연산속도
import time

t0 = time.time()
fib(35)
t1 = time.time()

total = t1 - t0
print(total) #=> 1.8418912887573242

#반복문 연산속도
import time

t0 = time.time()
fib_loop(10000)
t1 = time.time()

total = t1 - t0
print(total) #=> 0.005004167556762695