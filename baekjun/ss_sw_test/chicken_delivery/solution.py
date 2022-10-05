import sys

INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
CITY_MAP = [list(map(int, INPUT().split())) for _ in range(N)]


def get_distance(r_y, r_x, c_y, c_x):
    return abs(r_y - c_y) + abs(r_x - c_x)


def solution():
    global N, M, CITY_MAP

    chicken_coords = []
    house_coords = []
    for row in range(N):
        for col in range(N):
            if CITY_MAP[row][col] == 1:
                house_coords.append((row, col))
            if CITY_MAP[row][col] == 2:
                chicken_coords.append((row, col))

    def get_city_chicken_distance(curr_chicken_coords):
        nonlocal house_coords
        city_distance = 0
        for h_c in house_coords:
            house_distance = sys.maxsize
            for c_c in curr_chicken_coords:
                house_distance = min(get_distance(h_c[0], h_c[1], c_c[0], c_c[1]), house_distance)
            city_distance += house_distance
        return city_distance

    ret = sys.maxsize

    def backtracking(curr_idx, curr_chicken_coords):
        nonlocal ret, chicken_coords

        if len(curr_chicken_coords) == M:
            ret = min(get_city_chicken_distance(curr_chicken_coords), ret)
            return

        for idx in range(curr_idx, len(chicken_coords)):
            # TODO(joohyun): change to better way. I don't like coping.
            backup = curr_chicken_coords[:]
            curr_chicken_coords.append(chicken_coords[idx])
            backtracking(idx + 1, curr_chicken_coords)
            curr_chicken_coords = backup

    backtracking(0, curr_chicken_coords=[])

    return ret


ret = solution()
print(ret)
