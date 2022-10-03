import collections
import sys
import copy

inputs = sys.stdin.readline
N, M = map(int, inputs().split())
VIRUS_MAP = [list(map(int, inputs().split())) for _ in range(N)]

POS_VIRUS = []
POS_EMPTY = []

for row in range(N):
    for col in range(M):
        if VIRUS_MAP[row][col] == 0:
            POS_EMPTY.append((row, col))
        elif VIRUS_MAP[row][col] == 2:
            POS_VIRUS.append((row, col))

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
SOLUTION = 0


def check(virus_map):
    global POS_VIRUS, N, M

    # TODO(joohyun): change deepcopy
    tmp_virus_map = copy.deepcopy(virus_map)

    queue = collections.deque(POS_VIRUS)
    while queue:

        curr_y, curr_x = queue.popleft()

        for diff_y, diff_x in DIRECTIONS:

            new_y = curr_y + diff_y
            new_x = curr_x + diff_x

            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M or tmp_virus_map[new_y][new_x] != 0:
                continue

            tmp_virus_map[new_y][new_x] = 2
            queue.append((new_y, new_x))

    zero_cnt = 0
    for r in range(N):
        for c in range(M):
            if tmp_virus_map[r][c] == 0:
                zero_cnt += 1

    return zero_cnt


def backtracking(new_wall_count, curr_virus_map, empty_idx):
    global POS_EMPTY, SOLUTION

    if new_wall_count == 3:
        zero_cnt = check(curr_virus_map[:])
        SOLUTION = max(SOLUTION, zero_cnt)
        return

    for empty_idx in range(empty_idx, len(POS_EMPTY)):
        wall_y, wall_x = POS_EMPTY[empty_idx]
        tmp_virus_map = curr_virus_map[:]
        tmp_virus_map[wall_y][wall_x] = 1
        backtracking(new_wall_count + 1, tmp_virus_map, empty_idx + 1)
        tmp_virus_map[wall_y][wall_x] = 0


def solution():
    global N, M, VIRUS_MAP
    backtracking(new_wall_count=0, curr_virus_map=VIRUS_MAP[:], empty_idx=0)
    return SOLUTION


ret = solution()
print(ret)
