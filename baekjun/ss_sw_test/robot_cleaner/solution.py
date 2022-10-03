import collections
import sys

INPUTS = sys.stdin.readline
N, M = map(int, INPUTS().split())
ROBO_Y, ROBO_X, FIRST_DIR = map(int, INPUTS().split())
CLEAN_MAP = [list(map(int, INPUTS().split())) for _ in range(N)]

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def solution():
    global N, M, ROBO_Y, ROBO_X, FIRST_DIR, DIRECTIONS, CLEAN_MAP

    queue = collections.deque([(ROBO_Y, ROBO_X, FIRST_DIR)])

    ret = 0
    while queue:

        curr_y, curr_x, curr_dir = queue.popleft()

        if CLEAN_MAP[curr_y][curr_x] == 0:
            CLEAN_MAP[curr_y][curr_x] = 2
            ret += 1

        for dir_idx in range(len(DIRECTIONS)):
            next_dir = (curr_dir + 3 + (dir_idx * 3)) % 4
            diff_y, diff_x = DIRECTIONS[next_dir]
            next_y = diff_y + curr_y
            next_x = diff_x + curr_x

            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= M or CLEAN_MAP[next_y][next_x] != 0:
                continue

            queue.append((next_y, next_x, next_dir))
            break

        if len(queue) == 0:
            next_dir = curr_dir
            diff_y, diff_x = DIRECTIONS[(next_dir + 2) % 4]
            next_y = diff_y + curr_y
            next_x = diff_x + curr_x

            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= M or CLEAN_MAP[next_y][next_x] == 1:
                break

            queue.append((next_y, next_x, next_dir))

    return ret


ret = solution()
print(ret)
