#### 1. 간단한 N의 약수 (SWEA #1933)

- 입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.

```
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 =< N =< 1,000)

[입력]
입력으로 정수 N이 주어진다.

[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.

[입력 예시]
10

[출력 예시]
1 2 5 10
```

```
N = int(input('N은 1이상 1,000이하의 정수이다. (1 =< N =< 1.000): '))

for i in range(1, N+1):
    if N % i == 0:
        print(i, end = ' ')
```

```
N = int(input('N은 1이상 1,000이하의 정수이다. (1 =< N =< 1.000): '))

result = []
for i in range(1, N+1):
     if N % i == 0:
         result += [i]
print(*result)
```





#### 2. 중간값 찾기 (SWEA #2063 변형)

- 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

```
[출력 예시]
65
```

```
numbers = [
	85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
	51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
	52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
```

```
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
```





#### 3. 계단 만들기

- 자연수 number를 입력 받아, 아래와 같이 높이가 number인 내려가는 계단을 출력하시오.

```
[입력 예시]
4

[출력 예시]
1
1 2
1 2 3
1 2 3 4
```

```
N = int(input())
n = []

for i in range(1, N + 1):
    n += [i]
    print(*n)
```

