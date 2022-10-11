import collections

N, L, R = map(int, input().split())
POPULATION_MAP = [list(map(int, input().split())) for _ in range(N)]


def create_area(start_y, start_x, status, area_index, area_avg_list, total_visited):
    global N, L, R, POPULATION_MAP

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = collections.deque([(start_y, start_x)])
    total_visited.add((start_y, start_x))

    area_sum = 0
    area_count = 0
    while queue:

        curr_y, curr_x = queue.popleft()
        area_count += 1
        status[curr_y][curr_x] = area_index
        area_sum += POPULATION_MAP[curr_y][curr_x]

        for diff_y, diff_x in directions:
            next_y = curr_y + diff_y
            next_x = curr_x + diff_x

            if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N or ((next_y, next_x) in total_visited):
                continue

            population_diff = abs(POPULATION_MAP[next_y][next_x] - POPULATION_MAP[curr_y][curr_x])
            if not L <= population_diff <= R:
                continue

            total_visited.add((next_y, next_x))
            queue.append((next_y, next_x))

    area_avg_list.append(int(area_sum / area_count))


def solution():
    global N, L, R, POPULATION_MAP

    is_changed = True
    day_cnt = 0

    while is_changed:

        is_changed = False

        area_idx = 0
        area_avg_list = []
        total_visited = set()

        status = [[-1] * N for _ in range(N)]

        for row in range(N):
            for col in range(N):
                if (row, col) not in total_visited:
                    create_area(row, col, status, area_idx, area_avg_list, total_visited)
                    area_idx += 1

        for row in range(N):
            for col in range(N):
                index = status[row][col]
                area_avg = area_avg_list[index]
                if area_avg != POPULATION_MAP[row][col]:
                    is_changed = True
                    POPULATION_MAP[row][col] = area_avg

        if is_changed:
            day_cnt += 1

    return day_cnt


print(solution())
