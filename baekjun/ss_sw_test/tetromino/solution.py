import sys

inputs = sys.stdin.readline
N, M = map(int, inputs().split())
tetromino_map = [list(map(int, inputs().split())) for _ in range(N)]


def solution(n, m, tetromino_map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    ret = 0

    visited = [[False] * m for _ in range(n)]

    def dfs(y, x, curr_size, curr_sum):

        nonlocal ret, tetromino_map, visited

        if curr_size == 4:
            ret = max(curr_sum, ret)
            return

        for diff_y, diff_x in directions:

            new_y = y + diff_y
            new_x = x + diff_x

            if new_y < 0 or new_y >= n or new_x < 0 or new_x >= m or visited[new_y][new_x]:
                continue

            visited[new_y][new_x] = True
            dfs(new_y, new_x, curr_size=curr_size + 1, curr_sum=curr_sum + tetromino_map[new_y][new_x])
            visited[new_y][new_x] = False

    def cross_shape(y, x):

        nonlocal ret, tetromino_map, n, m

        for direction in range(4):

            curr_sum = tetromino_map[y][x]

            for step in range(3):
                curr_step = (step + direction) % 4
                new_y = y + directions[curr_step][0]
                new_x = x + directions[curr_step][1]

                if new_y < 0 or new_y >= n or new_x < 0 or new_x >= m:
                    curr_sum = 0
                    break

                curr_sum += tetromino_map[new_y][new_x]

            ret = max(ret, curr_sum)

    for row in range(n):
        for col in range(m):
            visited[row][col] = True
            dfs(y=row, x=col, curr_size=1, curr_sum=tetromino_map[row][col])
            visited[row][col] = False
            cross_shape(y=row, x=col)

    return ret


ret = solution(N, M, tetromino_map)
print(ret)
