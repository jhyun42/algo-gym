N = int(input())
DUST_MAP = [list(map(int, input().split())) for _ in range(N)]
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

WIND_Y = [
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],  # left
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],  # down
    [1, -1, 2, -2, 0, 1, -1, 1, -1],  # right
    [1, 1, 0, 0, -2, 0, 0, -1, -1],  # up
]

WIND_X = [
    [1, 1, 0, 0, -2, 0, 0, -1, -1],  # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],  # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],  # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],  # up
]

RATE = [1, 1, 2, 2, 5, 7, 7, 10, 10]


def wind(curr_r, curr_c, direction):
    ret = 0
    dust = DUST_MAP[curr_r][curr_c]
    dust_sum = 0
    for rate_idx in range(len(RATE)):

        new_r = curr_r + WIND_Y[direction][rate_idx]
        new_c = curr_c + WIND_X[direction][rate_idx]

        dust_wind = int((dust * RATE[rate_idx]) / 100)
        dust_sum += dust_wind

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
            ret += dust_wind
            continue

        DUST_MAP[new_r][new_c] += dust_wind

    # alpha 구하기
    new_r = curr_r + DIRECTIONS[direction][0]
    new_c = curr_c + DIRECTIONS[direction][1]

    alpha = (dust - dust_sum)
    if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
        ret += alpha
    else:
        DUST_MAP[new_r][new_c] += alpha

    DUST_MAP[curr_r][curr_c] = 0

    return ret


def solve(curr_r, curr_c):
    ret = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    dir_idx = -1

    while curr_r != 0 or curr_c != 0:

        visited[curr_r][curr_c] = True
        new_direction = (dir_idx + 1) % 4
        new_r = curr_r + DIRECTIONS[new_direction][0]
        new_c = curr_c + DIRECTIONS[new_direction][1]

        if visited[new_r][new_c]:
            new_direction = dir_idx
            new_r = curr_r + DIRECTIONS[new_direction][0]
            new_c = curr_c + DIRECTIONS[new_direction][1]

        ret += wind(new_r, new_c, new_direction)
        curr_r = new_r
        curr_c = new_c
        dir_idx = new_direction

    return ret


def solution():
    curr_r = N // 2
    curr_c = N // 2
    ret = solve(curr_r, curr_c)

    return ret


print(solution())

"""
    달팽이 travers 연습 
"""


def tornado_out_move():
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_idx = 0

    curr_r, curr_c = N // 2, N // 2
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[curr_r][curr_c] = True

    while True:

        diff_r, diff_c = directions[dir_idx]

        new_r = curr_r + diff_r
        new_c = curr_c + diff_c

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
            continue

        "Do something in here"

        if visited[new_r][new_c]:
            dir_idx = (4 + dir_idx - 1) % 4
            continue

        dir_idx = (4 + dir_idx + 1) % 4
        visited[new_r][new_c] = True
        curr_r = new_r
        curr_c = new_c

        if new_r == 0 and new_c == 0:
            break


def tornado_in_move():
    dir_idx = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    curr_r, curr_c = 0, 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[curr_r][curr_c] = True

    while True:

        diff_r, diff_c = directions[dir_idx]

        new_r = curr_r + diff_r
        new_c = curr_c + diff_c

        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N or visited[new_r][new_c]:
            dir_idx = (4 + dir_idx + 1) % 4
            continue

        "Do something in here"

        visited[new_r][new_c] = True
        curr_r = new_r
        curr_c = new_c

        if new_r == N // 2 and new_c == N // 2:
            break
