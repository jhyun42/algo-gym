import collections

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]


def solutions():
    global N, MAP
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    start_y, start_x = 0, 0
    for row in range(N):
        for col in range(N):
            if MAP[row][col] == 9:
                start_y, start_x = row, col
    MAP[start_y][start_x] = 0

    ret = 0

    shark_size = 2
    shark_time = 0
    shark_ate = 0

    is_changed = True
    while is_changed:
        is_changed = False

        queue = collections.deque([(start_y, start_x, shark_time)])
        visited = [[False] * N for _ in range(N)]
        visited[start_y][start_x] = True

        candi = (99, 0, -1)

        while queue:
            curr_y, curr_x, curr_time = queue.popleft()

            # 가장 가까운 물고기는 잡았다.
            candi_y, candi_x, candi_time = candi
            if (candi_time != -1) and (curr_time > candi_time):
                break

            # 먹을 수 있는 물고기 중 y 축이 작은 물고기를 선호하고, 같은 y축 상에 있을 때 x가 적은걸 선호한다.
            if MAP[curr_y][curr_x] < shark_size and MAP[curr_y][curr_x] != 0:
                is_changed = True
                if candi_y > curr_y or (candi_x > curr_x and candi_y == curr_y):
                    candi = (curr_y, curr_x, curr_time)

            for y_diff, x_diff in directions:

                new_y = curr_y + y_diff
                new_x = curr_x + x_diff

                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue

                if not visited[new_y][new_x] and MAP[new_y][new_x] <= shark_size:
                    visited[new_y][new_x] = True
                    queue.append((new_y, new_x, curr_time + 1))

        if is_changed:
            shark_y, shark_x, shark_time = candi
            shark_ate += 1
            if shark_ate == shark_size:
                shark_size += 1
                shark_ate = 0
            MAP[shark_y][shark_x] = 0
            start_y, start_x = shark_y, shark_x

    return shark_time


print(solutions())
