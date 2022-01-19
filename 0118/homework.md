#### 1. Mutable & Immutable

- 주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오.

```
String, List, Tuple, Range, Set, Dictionary
```

```
Mutable : List, Set, Dictionary
Immutable : String, Tuple, Range
```



#### 2. 홀수만 담기

- range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

```
odd_num = list(range(1, 51, 2))
print(odd_num)
```

```
odd_num = [i for i in range(1,51) if i % 2 ==1]
```



#### 3. Dictionary 만들기

- 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```
sudents = {박세은 : 25}
```



#### 4. 반복문으로 네모 출력

- 두 개의 정수 n과 m이 주어졌을 때,  가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

```
n = 5
m = 9
s = ''

for i in range(0,n):
    s += '*'
for i in range(0,m):
    print(s)
```



#### 5. 조건 표현식

- 주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.

```
temp = 36.5

if temp >= 37.5:
	print('입실 불가')
else:
	print('입실 가능')
```

```
temp = 36.5

status = '입실 불가' if temp >= 37.5 else '입실 가능'
print(status)
```



#### 6. 평균 구하기

- 주어진 list에 담긴 숫자들의 평균값을 출력하시오.

```
scores = [80, 89, 99, 83]
```

```
n = 0
total = 0

for i in scores:
    total +=i
    n += 1

avg = total/n
print(avg)
```

