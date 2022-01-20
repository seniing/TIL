#### 1. List의 합 구하기

- 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 **list_sum** 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```
list_sum([1, 2, 3, 4, 5]) #=> 15
```

```
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
    
print(list_sum([1, 2, 3, 4, 5])) #=> 15
```



#### 2. Dictionary로 이루어진 List의 합 구하기

- Dictionary로 이루어진 list를 전달 받아 모든 dictionary의 'age' key에 해당하는 value들의 합을 변환하는 **dict_list_sum** 함수를 built_in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```
dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]) #=> 16
```

```
def dict_list_sum(dict):
    total = 0
    for i in dict:
        for j in i:
            if 'age' == j:
                total += i[j]
    return total
    
print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])) #=> 16
```

```
def dict_list_sum(dict):
    total = 0
    for i in dict:
        total += i['age']
    return total
    
 print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}])) #=> 16
```



#### 3. 2차원 List의 전체 합 구하기

- 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 **list_sum** 함수를 buil-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

```
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) #=> 55
```

```
def all_list_sum(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j
    return total

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])) #=> 55
```



