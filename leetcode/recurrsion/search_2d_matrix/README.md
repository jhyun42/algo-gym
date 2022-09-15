# Search a 2D Matrix

## 1. 문제 설명

2D matrix에서 target값을 찾는 효율적인 알고리즘을 작성하여라.

### Example 1:

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

```

### Example 2:

```
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
```

### Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-109 <= matrix[i][j] <= 109`
- All the integers in each row are sorted in ascending order.
- All the integers in each column are sorted in ascending order. = `-109 <= target <= 109`

## 2. 문제 풀이

1. `left`,`right`,`up`,`down`을 매개변수로 받는 재귀함수를 생성한다.
2. 재귀함수는 두 개의 base case를 가진다
    1. 탐색하는 sub-matrix의 `left`가 `right`보다 클 때,
    2. `up`이 `down`클 때
3. Column을 sub-matrix의 중간(`mid`)으로 고정하고 `row` 변수를 현재 sub-matrix의 `up`으로 초기화한다.
4. `row`가 `down`만큼 증가할 때 까지 반복하여 값을 탐색한다.
5. 값을 찾으면 현재값을 return하고 찾지못하면 재귀함수를 초출한다. 재귀함수를 둘 호출 하는데
    1. 첫번째 재귀는 `right`를 `mid - 1`로, `up`을 `row`로 설정한다.
    2. 두번째 재귀는 `left`를 `mid + 1`로, `down`을 `row - 1`로 설정한다.

## 3. 시간 복잡도 & 공간 복잡도

(전반적으로 내용 추가 필요!)

### 시간복잡도

입력은 2차원 배열이고, 우선 $x = n^{2}$로 둔다.  
이때 시간 복잡도는 $2\cdot T(\frac{x}{4}) + \sqrt{x}$ 이다.  
$2\cdot T(\frac{x}{4})$는 sub-matrix로 나누고 그 중 재귀는 1/4만 사용한다는 점에서 발생하는 시간복잡도이고,  
$\sqrt{x}$는 각 재귀함수에서 `row`를 종단하면서 발생하는 시간복잡도이다.

### 공간복잡도

재귀가 진행되면서 사용하는 입력이 1/2씩 줄어들기 때문에 $log(n)$ 이상 넘어가지 않는다.

## 4. 코드

```python
def search_matrix(matrix, target):
    if not matrix:
        return False

    mat = matrix
    tg = target

    def search_rec(left, right, up, down):

        nonlocal mat
        nonlocal tg

        if left > right or up > down:
            return False

        elif tg > mat[down][right] or tg < mat[up][left]:
            return False

        mid = left + (right - left) // 2

        row = up
        while row <= down and mat[row][mid] <= tg:
            if mat[row][mid] == tg:
                return True

            row += 1

        return search_rec(left, mid - 1, row, down) or search_rec(mid + 1, right, up, row - 1)

    return search_rec(0, len(mat[0]) - 1, 0, len(mat) - 1)
```