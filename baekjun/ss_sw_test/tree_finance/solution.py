import collections

N, M, K = map(int, input().split())
A_MAP = [list(map(int, input().split())) for _ in range(N)]
PLANTED_INFO = [list(map(int, input().split())) for _ in range(M)]


# 나이가 어린 나무부터 먹는다
# 봄: 땅에 양분이 부족해 "자신의 나이"만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다
# 여름: 죽은 나무가 양분으로 변하게 된다. 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버림
# 가을: 나무가 번식한다 번식하는 나무는 나이가 5 배수 진접한 8개 칸에 나이가 1인 나무가 생김
# 겨울 땅을 돌아다니면서 땅에 양분을 추가. 각 칸에 추가 되는 양분의 양은 A[r][c]
# K 년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램?


def solution():
    global N, M, K, A_MAP, PLANTED_INFO
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    soil_map = [[5] * N for _ in range(N)]
    tree_map = [[[] for _ in range(N)] for _ in range(N)]

    for y, x, age in PLANTED_INFO:
        tree_map[y - 1][x - 1].append(age)

    for _ in range(K):

        # Spring N Summer
        for row in range(N):
            for col in range(N):

                if len(tree_map[row][col]) == 0:
                    continue

                if len(tree_map[row][col]) > 1:
                    tree_map[row][col].sort()

                tmp_tree, dead_tree = [], 0
                for age in tree_map[row][col]:
                    if age <= soil_map[row][col]:
                        soil_map[row][col] -= age
                        age += 1
                        tmp_tree.append(age)
                    else:
                        dead_tree += age // 2

                soil_map[row][col] += dead_tree
                tree_map[row][col] = tmp_tree

        if not tree_map:
            return 0

        # Autumn
        for row in range(N):
            for col in range(N):

                if len(tree_map[row][col]) == 0:
                    continue

                for age in tree_map[row][col]:
                    if age % 5 == 0:
                        for y_diff, x_diff in directions:

                            new_row = row + y_diff
                            new_col = col + x_diff

                            if new_row < 0 or new_row >= N or new_col < 0 or new_col >= N:
                                continue

                            tree_map[new_row][new_col].append(1)

        # Winter
        for row in range(N):
            for col in range(N):
                soil_map[row][col] += A_MAP[row][col]

    # 나무 개수 출력
    tree_cnt = 0
    for row in range(N):
        for col in range(N):
            tree_cnt += len(tree_map[row][col])

    return tree_cnt


print(solution())
