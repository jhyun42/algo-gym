import copy
import sys

INPUT = sys.stdin.readline
N, M = map(int, INPUT().split())
MAP = [list(map(int, INPUT().split())) for _ in range(N)]


def solution():
    global MAP, N, M

    ret = float('inf')
    rot_possibilities = [4, 2, 4, 4, 1]

    pos_cctv = []
    for row in range(N):
        for col in range(M):
            if MAP[row][col] != 0 and MAP[row][col] != 6:
                pos_cctv.append((row, col, MAP[row][col]))

    def copy_map(dest, src):
        for r in range(N):
            for c in range(M):
                dest[r][c] = src[r][c]

    def update(direction, curr_cctv):
        global MAP

        direction = direction % 4

        # East
        if direction == 0:
            for c in range(curr_cctv[1] + 1, M):
                if MAP[curr_cctv[0]][c] == 6:
                    break
                MAP[curr_cctv[0]][c] = -1

        # North

        elif direction == 1:
            for r in reversed(range(curr_cctv[0])):
                if MAP[r][curr_cctv[1]] == 6:
                    break
                MAP[r][curr_cctv[1]] = -1

        # West
        elif direction == 2:
            for c in reversed(range(curr_cctv[1])):
                if MAP[curr_cctv[0]][c] == 6:
                    break
                MAP[curr_cctv[0]][c] = -1

        # South
        elif direction == 3:
            for r in range(curr_cctv[0] + 1, N):
                if MAP[r][curr_cctv[1]] == 6:
                    break
                MAP[r][curr_cctv[1]] = -1

    def backtracking(cctv_idx):

        global MAP
        nonlocal ret, pos_cctv, rot_possibilities

        if cctv_idx == len(pos_cctv):
            zero_cnt = 0
            for r in range(N):
                for c in range(M):
                    if MAP[r][c] == 0:
                        zero_cnt += 1
            ret = min(ret, zero_cnt)
            return

        curr_cctv_type = pos_cctv[cctv_idx][-1] - 1
        for direction in range(rot_possibilities[curr_cctv_type]):
            backup_map = [[0] * M for _ in range(N)]
            copy_map(backup_map, MAP)

            if curr_cctv_type == 0:
                update(direction=direction, curr_cctv=pos_cctv[cctv_idx])

            if curr_cctv_type == 1:
                update(direction=direction, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 2, curr_cctv=pos_cctv[cctv_idx])

            if curr_cctv_type == 2:
                update(direction=direction, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 1, curr_cctv=pos_cctv[cctv_idx])

            if curr_cctv_type == 3:
                update(direction=direction, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 1, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 2, curr_cctv=pos_cctv[cctv_idx])

            if curr_cctv_type == 4:
                update(direction=direction, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 1, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 2, curr_cctv=pos_cctv[cctv_idx])
                update(direction=direction + 3, curr_cctv=pos_cctv[cctv_idx])

            backtracking(cctv_idx + 1)
            copy_map(MAP, backup_map)

    backtracking(0)

    return ret


ret = solution()
print(ret)
