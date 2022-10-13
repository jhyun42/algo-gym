N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
MAP_2 = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for R in range(1, N + 1):
    for C in range(1, N + 1):
        MAP_2[R][C] = MAP[R - 1][C - 1]

INF = 10000000000000


def solve(row, col, d_1, d_2, total_population):
    global N, MAP_2

    temp_map = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    temp_map[row][col] = 5

    for idx in range(1, d_1 + 1):
        temp_map[row + idx][col - idx] = 5
        temp_map[row + d_2 + idx][col + d_2 - idx] = 5

    for idx in range(1, d_2 + 1):
        temp_map[row + idx][col + idx] = 5
        temp_map[row + d_1 + idx][col - d_1 + idx] = 5

    area_1 = 0
    for r in range(1, row + d_1):
        for c in range(1, col + 1):
            if temp_map[r][c] == 5:
                break
            area_1 += MAP_2[r][c]

    area_2 = 0
    for r in range(1, row + d_2 + 1):
        for c in reversed(range(col + 1, N + 1)):
            if temp_map[r][c] == 5:
                break
            area_2 += MAP_2[r][c]

    area_3 = 0
    for r in range(row + d_1, N + 1):
        for c in range(1, col - d_1 + d_2):
            if temp_map[r][c] == 5:
                break
            area_3 += MAP_2[r][c]

    area_4 = 0
    for r in range(row + d_2 + 1, N + 1):
        for c in reversed(range(col - d_1 + d_2, N + 1)):
            if temp_map[r][c] == 5:
                break
            area_4 += MAP_2[r][c]

    area_5 = total_population - area_1 - area_2 - area_3 - area_4

    max_val = max(area_1, max(area_2, max(area_3, max(area_4, area_5))))
    min_val = min(area_1, min(area_2, min(area_3, min(area_4, area_5))))
    return max_val - min_val


def solution():
    global N, MAP_2

    total_population = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            total_population += MAP_2[r][c]

    ret = INF
    for start_r in range(1, N + 1):
        for start_c in range(1, N + 1):
            for d_1 in range(1, N + 1):
                for d_2 in range(1, N + 1):
                    # 나와있는 조건 1
                    if start_r + d_1 + d_2 > N:
                        continue
                    # 나와있는 조건 2
                    if 1 > start_c - d_1:
                        continue
                    # 나와있는 조건 3
                    if start_c + d_2 > N:
                        continue

                    ret = min(ret, solve(start_r, start_c, d_1, d_2, total_population))

    return ret


print(solution())
