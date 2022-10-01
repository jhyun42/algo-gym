import collections
import sys

inputs = sys.stdin.readline

n, m = map(int, inputs().split())
input_map = [list(inputs().strip()) for _ in range(n)]


def solution(n, m, input_map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    row_len = n
    col_len = m

    blue_start_y, blue_start_x = 0, 0
    red_start_y, red_start_x = 0, 0

    for row in range(row_len):
        for col in range(col_len):

            if input_map[row][col] == 'R':
                red_start_y, red_start_x = row, col

            if input_map[row][col] == 'B':
                blue_start_y, blue_start_x = (row, col)

    visited = [[[[False] * col_len for _ in range(row_len)] for _ in range(col_len)] for _ in range(row_len)]
    visited[red_start_y][red_start_x][blue_start_y][blue_start_x] = True

    queue = collections.deque([(red_start_y, red_start_x, blue_start_y, blue_start_x, 0)])

    ret = -1

    def move(y, x, y_diff, x_diff):
        while True:
            if input_map[y][x] != '#' and input_map[y][x] != 'O':
                y += y_diff
                x += x_diff
            else:
                if input_map[y][x] == '#':
                    y -= row_diff
                    x -= col_diff
                return y, x

    while queue:
        curr_red_y, curr_red_x, curr_blue_y, curr_blue_x, curr_move_cnt = queue.popleft()

        if curr_move_cnt > 10:
            break

        if input_map[curr_red_y][curr_red_x] == 'O' and input_map[curr_blue_y][curr_blue_x] != 'O':
            ret = curr_move_cnt
            break

        for row_diff, col_diff in directions:

            next_red_y = curr_red_y
            next_red_x = curr_red_x
            next_blue_y = curr_blue_y
            next_blue_x = curr_blue_x

            next_red_y, next_red_x = move(next_red_y, next_red_x, y_diff=row_diff, x_diff=col_diff)
            next_blue_y, next_blue_x = move(next_blue_y, next_blue_x, y_diff=row_diff, x_diff=col_diff)

            if (next_red_y == next_blue_y) and (next_red_x == next_blue_x):
                if input_map[next_red_y][next_red_x] != 'O':
                    red_dist = abs(next_red_y - curr_red_y) + abs(next_red_x - curr_red_x)
                    blue_dist = abs(next_blue_y - curr_blue_y) + abs(next_blue_x - curr_blue_x)
                    if red_dist > blue_dist:
                        next_red_y -= row_diff
                        next_red_x -= col_diff
                    else:
                        next_blue_y -= row_diff
                        next_blue_x -= col_diff

            if not visited[next_red_y][next_red_x][next_blue_y][next_blue_x]:
                visited[next_red_y][next_red_x][next_blue_y][next_blue_x] = True
                queue.append((next_red_y, next_red_x, next_blue_y, next_blue_x, curr_move_cnt + 1))

    return ret


ret = solution(n, m, input_map)
print(ret)
