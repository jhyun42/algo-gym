import sys

INPUT = sys.stdin.readline
N = int(INPUT())
D_CURVE_INFO = [list(map(int, INPUT().split())) for _ in range(N)]


def solution():
    global D_CURVE_INFO, N

    d_curve_map = [[False] * 102 for _ in range(102)]
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    for x, y, direction, generation in D_CURVE_INFO:
        d_curve_map[y][x] = True

        d_curve_order = [0] * (2 ** generation)
        num_curves = 0
        d_curve_order[num_curves] = direction
        num_curves += 1

        for g_idx in range(generation):
            for curve_idx in reversed(range(num_curves)):
                d_curve_order[num_curves] = (d_curve_order[curve_idx] + 1) % 4
                num_curves += 1

        for d_c in d_curve_order:
            diff_y, diff_x = directions[d_c]
            new_y = diff_y + y
            new_x = diff_x + x

            if new_y < 0 or new_y >= 102 or new_x < 0 or new_x >= 102:
                continue

            d_curve_map[new_y][new_x] = True
            y = new_y
            x = new_x

    ret = 0
    for row in range(102):
        for col in range(102):
            if d_curve_map[row][col] and d_curve_map[row][col + 1] \
                    and d_curve_map[row + 1][col] and d_curve_map[row + 1][col + 1]:
                ret += 1

    return ret


ret = solution()
print(ret)
