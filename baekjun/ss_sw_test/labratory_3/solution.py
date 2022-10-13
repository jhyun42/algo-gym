import collections
import sys

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INF = sys.maxsize


def activate_virus(curr_active_virus_list):
    global N, MAP
    empty_count = 0
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 0:
                empty_count += 1

    queue = collections.deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for virus_y, virus_x in curr_active_virus_list:
        queue.append((virus_y, virus_x, 0))
        visited[virus_y][virus_x] = 1

    while queue:
        curr_y, curr_x, curr_time = queue.popleft()
        if MAP[curr_y][curr_x] == 0:
            empty_count -= 1

        if empty_count == 0:
            return curr_time

        for diff_y, diff_x in DIRECTIONS:
            next_y = diff_y + curr_y
            next_x = diff_x + curr_x
            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N:
                continue
            if visited[next_y][next_x] == 0 and MAP[next_y][next_x] != 1:
                queue.append((next_y, next_x, curr_time + 1))
                visited[next_y][next_x] = True

    return INF


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
