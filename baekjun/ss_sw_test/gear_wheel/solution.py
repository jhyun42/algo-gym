import sys

INPUT = sys.stdin.readline
GEAR_1 = list(map(int, INPUT().strip()))
GEAR_2 = list(map(int, INPUT().strip()))
GEAR_3 = list(map(int, INPUT().strip()))
GEAR_4 = list(map(int, INPUT().strip()))
NUM_ROTATION = int(INPUT())
ROTATION_INFO = [list(map(int, INPUT().split())) for _ in range(NUM_ROTATION)]


def rotate(gear, direction):
    if direction == 1:
        gear = [gear[-1]] + gear[:-1]

    elif direction == -1:
        gear = gear[1:] + [gear[0]]

    return gear


def solution():
    global GEAR_1, GEAR_2, GEAR_3, GEAR_4, ROTATION_INFO
    gears = [GEAR_1, GEAR_2, GEAR_3, GEAR_4]

    for gear_num, direction in ROTATION_INFO:
        gear_num -= 1

        move_cmd = [0] * 4
        move_cmd[gear_num] = direction

        for left in reversed(range(gear_num)):

            right = left + 1
            if gears[left][2] == gears[right][6]:
                break
            else:
                move_cmd[left] = move_cmd[right] * -1

        for right in range(gear_num + 1, 4):
            left = right - 1
            if gears[left][2] == gears[right][6]:
                break
            else:
                move_cmd[right] = move_cmd[left] * -1

        for g_idx in range(len(gears)):
            gears[g_idx] = rotate(gears[g_idx], move_cmd[g_idx])

    ret = 0
    for g_idx in range(len(gears)):
        if gears[g_idx][0] == 1:
            ret += (1 << g_idx)

    return ret


ret = solution()
print(ret)
