# Remove Element

## 1. 문제 설명

정수 배열 nums와 정수 val이 주어졌을 때 nums에서 val의 모든 항목을 in-place로 제거하는 함수를 작성하여라.  
요소의 상대적 순서는 변경될 수 있다.

일부 언어에서는 배열의 길이를 변경할 수 없으므로 결과를 배열 nums의 첫 번째 부분에 배치하면 된다.  
부가적으로 설명하면, 제거하려는 요소를 제거한 후 k개의 요소가 있으면 nums의 처음 k개의 요소가 최종 결과를 나타내면 된다.  
처음 k개 요소를 넘어 무엇을 남겨두는지는 중요하지 않다.

nums의 처음 k개의 슬롯에 최종 결과를 배치한 후 k를 반환하라.

In-place로 제거해야하기 떄문에 추가 공간을 할당하면 안된다 (SC = $O(1)$).

### Example 1:

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Example 2:

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Constraints:

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

## 2. 문제 풀이

투 포인터 접근으로 풀면된다.

1. 입력 `nums` 어래이를 횡단하는 포인터 `idx`와 어래이의 요소를 수정하려는 위치의 포인터 `k`를 생성한다.
2. `nums[idx]`가 지우려는 숫자 `val`과 같지 않다면 현재 수정하려는 `nums[k]`을 `nums[idx]`로 체우고 `k`를 +1 한다.
3. 결과 어래이의 요소 개수인 `k`를 반환해야하기 때문에 현제 `k`를 반환한다.

## 3. 시간 복잡도 & 공간 복잡도

전체 입력 리스트를 한번만 횡단하면 되기 때문에 시간 복잡도는 $O(N)$,  
공간 복잡도는 새로운 list 를 생성하지 않기 때문에 $O(1)$.

## 4. 코드

```python
def remove_element(nums, val):
    len_nums = len(nums)
    k = 0

    for idx in range(len_nums):

        if nums[idx] != val:
            nums[k] = nums[idx]
            k += 1

    return k
```