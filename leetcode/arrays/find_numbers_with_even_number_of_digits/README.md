# Find Numbers with Even Number of Digits

## 1. 문제 설명

정수의 배열이 주어졌을 때, 자릿수가 짝수인 정수의 개수를 반환하라.

### Example 1:

```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

### Example 2:

```
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
```

## 2. 문제 풀이

배열의 값들을 확인한다. 각각의 값을 10으로 계속해서 10 이하가 될 때까지 나누면서 숫자 개수 count (digit count) 를 할 수 있고,  
digit count 를 modular 연산을 통해 짝수인지 홀수인지 확인하여 짝수면 return 할 count 값을 +1 한다.

## 3. 시간 복잡도 & 공간 복잡도

전체 입력 리스트를 한번만 횡단하면 되기 때문에 시간 복잡도는 $O(N)$,  
공간 복잡도는 따로 list 를 생성하거나 하지 않기 때문에 $O(1)$.

## 4. 코드

```python
from typing import List


def find_numbers(nums: List[int]) -> int:
    num_even = 0
    for num in nums:

        digits_cnt = 1

        while num >= 10:
            digits_cnt += 1
            num //= 10

        if digits_cnt % 2 == 0:
            num_even += 1

    return num_even
```