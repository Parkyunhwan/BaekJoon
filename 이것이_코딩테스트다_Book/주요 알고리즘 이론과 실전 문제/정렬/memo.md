# 정렬
### 선택정렬
* 매번 `가장 작은 데이터를 선택`해 앞으로 보낸다.
* 시간 복잡도 `O(N^2)`
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
```

### 삽입 정렬
* `두번 째` 데이터부터 시작한다. (첫번째는 정렬되어 있다 판단)
* 현재 선택한 데이터를 앞에 정렬되어 있는 리스트의 적절한 위치를 찾아 삽입한다.
    * ex) 3이라면 1과 5 사이에 삽입.
* 자신보다 작은 데이터를 만나면 바로 멈추고 그 위치에 삽입한다.
    * 자신보다 작은 데이터 이후의 검사는 이미 정렬되어 있어 해보나 마나다.
    
* 삽입정렬의 시간복잡도는 `O(N^2)`이지만 거의 정렬된 리스트라면 `O(N)`에 비슷한 속도를 낸다.
* 따라서,  `거의 정렬이 되어 있는 상태`에서는 삽입정렬을 사용하는 것이 굉장히 `효율적`이다.
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
```

### 퀵정렬

* `기준 데이터(pivot)를 기반으로 큰 데이터와 작은 데이터의 자리 교체`
* 퀵정렬의 평균 시간 복잡도는 `O(NlogN)`이다. 그러나 데이터가 이미 정렬되어 있는 경우에는 `O(N^2)`으로 매우 느리게 동작한다.
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
```

* 다음은 `파이썬 특화 퀵 정렬` 코드이다.
```python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
리스트의 특징을 이용해서 간단히 구현했지만 엇갈렸을 때 종료되지 않기 때문에 비교 연산의 횟수는 증가한다.

### 계수 정렬

* `특정한 조건`이 부합할 때만 사용할 수 있는 **매우 빠른 알고리즘**
* 데이터의 개수 N, 데이터 중 최댓값 K일 때, 수행시간 O(N + K)를 보장한다.
* 일반적으로 데이터의 크기가 1,000,000(백만)을 넘지 않을 때 사용
* 비교 기반 알고리즘이 아님.
* 모든 리스트의 데이터를 확인하며 인덱스의 값을 증가시킴
* 나온 결과 리스트를 중복 횟수만큼 출력하면 된다.
* 계수 정렬의 공간 복잡도는 O(N + K) 이다.
```python
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력
```
## 코딩테스트의 3가지 유형

1. 정렬 라이브러리로 푸는 문제
2. 정렬 알고리즘의 원리를 묻는 문제
3. 더 빠른 정렬이 필요한 문제