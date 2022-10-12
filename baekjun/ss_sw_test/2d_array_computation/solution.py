R, C, K = map(int, input().split())
ARRAY = [list(map(int, input().split())) for _ in range(3)]


# R 연산 -> C 연산
# 한 행 또는 열에 있는 수 정렬 -> 각각의 수 가 몇번 나왔는지 알아야함
# 수의 등장 회수가 커지는 순으로, 그러한것이 여러가지면 수가 커지는 순으로 정렬
# A 에 길어진 결과를 다시 넣음
# 수의 등장 횟수가 커지는 순,
# A[R][C] = K 가 되는 최소 시간을 구하여라
# [3, 1, 1] 3이 1번 1 가 2번

def update(mat, direction):
    new_mat, length = [], 0  # 연산 후 반환할 행열, 최대 길이 행(또는 열)을 위한 변수

    for row in mat:
        num_cnt, new_row = [], []  # (숫자, 개수)를 담을 배열, 연산 후의 행(또는 열)을 담을 배열
        for num in set(row):

            # padding을 위해 채워 넣은 0일 경우 무시
            if num == 0:
                continue

            cnt = row.count(num)
            num_cnt.append((num, cnt))

        # 문제에서 제시하는 정렬방법
        num_cnt = sorted(num_cnt, key=lambda x: (x[1], x[0]))
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_mat.append(new_row)
        length = max(length, len(new_row))

    for row in new_mat:

        row += [0] * (length - len(row))

        if len(row) > 100:
            row = row[:100]

    return list(zip(*new_mat)) if direction == 'C' else new_mat


def solution():
    global R, C, K, ARRAY

    ret = 0

    while True:

        # 시간이 100이 넘으면 break
        if ret > 100:
            ret = -1
            break

        # A[R][C]의 값이 R이 되면 break
        if 0 <= R - 1 < len(ARRAY) and 0 <= C - 1 < len(ARRAY[0]) and ARRAY[R - 1][C - 1] == K:
            break
        if len(ARRAY) >= len(ARRAY[0]):
            ARRAY = update(ARRAY, 'R')
        else:
            ARRAY = update(list(zip(*ARRAY)), 'C')

        ret += 1

    return ret


print(solution())
