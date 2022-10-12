import math

R, C, T = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(R)]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def diffusion_update():
    global R, C, MAP
    tmp_map = [[0 for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):

            if MAP[row][col] == 0:
                continue

            elif MAP[row][col] == -1:
                tmp_map[row][col] = MAP[row][col]
                continue

            cell_dust = MAP[row][col]
            diffused_cell_cnt = 0

            for diff_y, diff_x in DIRECTIONS:

                new_row = row + diff_y
                new_col = col + diff_x

                if new_row < 0 or new_row >= R or new_col < 0 or new_col >= C or MAP[new_row][new_col] == -1:
                    continue

                diffused_cell_cnt += 1
                tmp_map[new_row][new_col] += math.trunc(cell_dust / 5)

            tmp_map[row][col] += MAP[row][col] - (math.trunc(cell_dust / 5) * diffused_cell_cnt)

    MAP = tmp_map


def circulate_update():
    global R, C, MAP

    circulator_pos = []
    for row in range(R):
        for col in range(C):
            if MAP[row][col] == -1:
                circulator_pos.append((row, col))

    lower_row = circulator_pos[0][0]
    upper_row = circulator_pos[1][0]

    # Upper anti-clockwise
    MAP[lower_row - 1][0] = 0
    for row in reversed(range(1, lower_row)):
        MAP[row][0] = MAP[row - 1][0]

    for col in range(C - 1):
        MAP[0][col] = MAP[0][col + 1]

    for row in range(lower_row):
        MAP[row][C - 1] = MAP[row + 1][C - 1]

    for col in reversed(range(1, C - 1)):
        MAP[lower_row][col + 1] = MAP[lower_row][col]
    MAP[lower_row][1] = 0

    # Lower clockwise
    MAP[upper_row + 1][0] = 0
    for row in range(upper_row + 1, R - 1):
        MAP[row][0] = MAP[row + 1][0]

    for col in range(C - 1):
        MAP[R - 1][col] = MAP[R - 1][col + 1]

    for row in reversed(range(upper_row + 1, R)):
        MAP[row][C - 1] = MAP[row - 1][C - 1]

    for col in reversed(range(1, C - 1)):
        MAP[upper_row][col + 1] = MAP[upper_row][col]
    MAP[upper_row][1] = 0


def solution():
    global R, C, T, MAP

    for _ in range(T):
        diffusion_update()
        circulate_update()

    ret = 0
    for row in range(R):
        for col in range(C):
            if MAP[row][col] > 0:
                ret += MAP[row][col]

    return ret


print(solution())
