import sys

inputs = sys.stdin.readline
y_len, x_len, start_y, start_x, k = map(int, inputs().split())
dice_map = [list(map(int, inputs().split())) for _ in range(y_len)]
cmd_order = list(map(int, inputs().split()))


def solution(y_len, x_len, start_x, start_y, dice_map, cmd_order):
    num_commands = len(cmd_order)

    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    dice_eyes = [0] * 6

    def roll_dice(dice_eyes, cmd):

        if cmd == 0:
            dice_eyes[0], dice_eyes[2], dice_eyes[3], dice_eyes[5] = \
                dice_eyes[2], dice_eyes[5], dice_eyes[0], dice_eyes[3]
        elif cmd == 1:
            dice_eyes[0], dice_eyes[2], dice_eyes[3], dice_eyes[5] = \
                dice_eyes[3], dice_eyes[0], dice_eyes[5], dice_eyes[2]
        elif cmd == 2:
            dice_eyes[0], dice_eyes[1], dice_eyes[4], dice_eyes[5] = \
                dice_eyes[1], dice_eyes[5], dice_eyes[0], dice_eyes[4]
        elif cmd == 3:
            dice_eyes[0], dice_eyes[1], dice_eyes[4], dice_eyes[5] = \
                dice_eyes[4], dice_eyes[0], dice_eyes[5], dice_eyes[1]

        return dice_eyes

    curr_x = start_x
    curr_y = start_y

    dice_eyes[0] = dice_map[curr_y][curr_x]

    for idx in range(num_commands):
        curr_cmd = cmd_order[idx] - 1

        new_y = curr_y + directions[curr_cmd][0]
        new_x = curr_x + directions[curr_cmd][1]

        if new_y < 0 or new_y >= y_len or new_x < 0 or new_x >= x_len:
            continue

        dice_eyes = roll_dice(dice_eyes, cmd=curr_cmd)

        if dice_map[new_y][new_x] == 0:
            dice_map[new_y][new_x] = dice_eyes[0]

        else:
            dice_eyes[0] = dice_map[new_y][new_x]
            dice_map[new_y][new_x] = 0

        curr_y = new_y
        curr_x = new_x

        print(dice_eyes[5])


solution(y_len, x_len, start_x, start_y, dice_map, cmd_order)
