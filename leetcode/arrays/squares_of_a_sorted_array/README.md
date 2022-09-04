# Squares of a Sorted Array

## 1. 문제 설명

오름차순으로 정렬된 정수 배열이 주어질 때, 오름차순으로 정렬된 각 숫자의 제곱 배열을 반환하라.

### Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

### Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

### Constraints:

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- nums is sorted in non-decreasing order.

## 2. 문제 풀이

### Approach 1. 정렬

음수 제곱을 고려해 우선 모든 숫자들의 제곱을 계산하고 정렬을 진행.

### Approach 2. 투 포인터

음수의 제곱이 양수의 제곱보다 클 수 있으므로 왼쪽과 오른쪽을 같이 고려해야 한다.

1. 반환을 위해 입력 리스트와 같은 크기의 `result_list` 생성.
2. 리스트의 양끝 포인터인 `left`와 `right`를 생성.
3. `for idx in range(len(nums) - 1, -1, -1)` 을 통해 역순으로 `result_list` 리스트를 횡단.
4. `nums[left]`의 **절대값**과 `nums[right]` **절대값**을 비교하여 큰 둘중에서 **큰 값**을 제곱하여 `result_list` 의 뒤 부터 채워 넣는다.

## 3. 시간 복잡도 & 공간 복잡도

### Approach 1. 정렬

시간 복잡도는 sort 를 진행한다는 점을 고려하여 $O(N log N)$. N 은 array 의 길이.  
공간 복잡도는 sort 알고리즘에서 발생하는 $O(N)$.

### Approach 2. 투 포인터

시간 복잡도는 전체 입력 리스트를 한번만 횡단하면 되기 때문에 $O(N)$.  
공간 복잡도는 input array 와 크기가 같은 result list 를 생성하기 때문에 $O(N)$.

## 4. 코드

### Approach 1. 정렬

```python
def sorted_squares(nums):
    return sorted(x * x for x in nums)
```

### Approach 2. 투 포인터

```python
def sorted_squares(nums):
    num_nums = len(nums)

    result_list = [0] * num_nums

    left = 0
    right = num_nums - 1

    for i in range(num_nums - 1, -1, -1):

        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1

        else:
            square = nums[left]
            left += 1

        result_list[i] = square * square

    return result_list
```