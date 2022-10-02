import sys

inputs = sys.stdin.readline

N = int(inputs())
K = int(inputs())
pos_apple = [list(map(int, inputs().split())) for _ in range(K)]
L = int(inputs())
t_and_rot = {}
for _ in range(L):
    t, rot = inputs().split()
    t_and_rot[int(t)] = rot


def solution(n, k, position_apple, l, time_and_rotation: dict):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    curr_dir = 0
    timestamp = 0

    head_y, head_x = 0, 0
    snake_pos_list = [(head_y, head_x)]
    snake_tail_idx = timestamp

    snake_map = [[0] * n for _ in range(n)]
    snake_map[head_y][head_x] = -1

    for p_a in position_apple:
        # do -1 because to change to index of list
        snake_map[p_a[0] - 1][p_a[1] - 1] = 1

    while True:

        timestamp += 1
        head_y += directions[curr_dir][0]
        head_x += directions[curr_dir][1]

        if (head_y < 0) or (head_y >= n) or (head_x < 0) or (head_x >= n):
            break

        if snake_map[head_y][head_x] == -1:
            break

        snake_pos_list.append((head_y, head_x))
        if snake_map[head_y][head_x] == 0:
            tail_y = snake_pos_list[snake_tail_idx][0]
            tail_x = snake_pos_list[snake_tail_idx][1]
            snake_map[tail_y][tail_x] = 0
            snake_tail_idx += 1

        snake_map[head_y][head_x] = -1
        curr_cmd = time_and_rotation.get(timestamp, False)
        if curr_cmd:
            if curr_cmd == 'D':
                curr_dir = (curr_dir + 1) % 4

            if curr_cmd == 'L':
                curr_dir = (curr_dir + 3) % 4

    return timestamp


ret = solution(n=N, k=K, position_apple=pos_apple, l=L, time_and_rotation=t_and_rot)
print(ret)
