# Find Pivot Index

## 1. 문제 설명

정수의 배열이 주어졌을 때, 해당 배열의 pivot index 를 구하라.

- Pivot index 란 index 왼쪽에 있는 모든 숫자의 합이 index 오른쪽에 있는 모든 숫자의 합이 같은 index 다.
- Index 가 배열의 왼쪽 가장자리에 있으면 왼쪽에 요소가 없기 때문에 왼쪽 합계는 0이다.  
  array 의 오른쪽 가장자리에도 적용된다.
- 가장 왼쪽의 pivot 를 반환하라. 만약 pivot index 가 존재하지 않으면 -1을 반환하라.

### Example 1:

```
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

### Example 2:

```
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

### Example 3:

```
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
```

### Constraints:

- `1 <= nums.length <= 104`
- `-1000 <= nums[i] <= 1000`

## 2. 문제 풀이

1. list 전체 합을 `nums_sum = sum(nums)`를 통해 구한다.
2. 리스트를 횡단하면서 running sum 을 저장할 left_sum 변수를 생성한다.
3. list 를 횡단하면서 `left_sum == (nums_sum - left_sum - curr_element)`를 만족시키면 현재 index 를 반환.
4. 3번의 조건을 만족시키지 못하면 -1를 반환.

## 3. 시간 복잡도 & 공간 복잡도

전체 입력 리스트를 한번만 횡단하면 되기 때문에 시간 복잡도는 $O(N)$,  
공간 복잡도는 따로 list 를 생성하거나 하지 않기 때문에 $O(1)$.

## 4. 코드

```python
def pivot_index(nums):
    nums_sum = sum(nums)
    left_sum = 0

    for i, x in enumerate(nums):

        if left_sum == (nums_sum - left_sum - x):
            return i
        left_sum += x

    return -1
```