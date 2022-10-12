# 맞왜틀?

import sys

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INF = sys.maxsize


def activate_virus(curr_active_virus_list):
    global N, MAP

    map_copy = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            map_copy[row][col] = MAP[row][col]
            if map_copy[row][col] == 2 and (row, col) not in curr_active_virus_list:
                map_copy[row][col] = -1

    ret = 0
    prev_virus_list = list(curr_active_virus_list)
    is_updated = True

    while is_updated:

        is_updated = False
        tmp_virus_list = prev_virus_list
        prev_virus_list = []

        for virus_y, virus_x in tmp_virus_list:

            for diff_y, diff_x in DIRECTIONS:
                new_y = virus_y + diff_y
                new_x = virus_x + diff_x

                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue

                if map_copy[new_y][new_x] != 0:
                    if map_copy[new_y][new_x] == -1:
                        map_copy[new_y][new_x] = 2
                        prev_virus_list.append((new_y, new_x))
                    continue

                map_copy[new_y][new_x] = 2
                prev_virus_list.append((new_y, new_x))
                is_updated = True

        if is_updated:
            ret += 1

    for row in range(N):
        for col in range(N):
            if map_copy[row][col] == 0:
                return INF

    return ret


def solution():
    global N, M, MAP

    virus_pos = []
    wall_pos = []

    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 2:
                virus_pos.append((row, col))
            elif MAP[row][col] == 1:
                wall_pos.append((row, col))

    ret = INF

    def backtracking(curr_active_virus_set, start_idx):
        nonlocal ret

        if len(curr_active_virus_set) == M:
            ret = min(activate_virus(curr_active_virus_set), ret)
            return

        for v_idx in range(start_idx, len(virus_pos)):
            curr_active_virus_set.add(virus_pos[v_idx])
            backtracking(curr_active_virus_set, start_idx=v_idx + 1)
            curr_active_virus_set.remove(virus_pos[v_idx])

    backtracking(set(), 0)

    if ret == INF:
        return -1

    return ret


print(solution())
