import collections

R, C, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
WALL_INFO = [list(map(int, input().split())) for _ in range(W)]

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 히터의 좌표와 방향을 저장
HEATERS = []

# 지속 적으로 체크할 공간
CHECK_AREA = []

for row in range(R):
    for col in range(C):
        if MAP[row][col] == 0:
            continue

        elif MAP[row][col] == 5:
            CHECK_AREA.append((row, col))

        else:
            HEATERS.append((row, col, MAP[row][col] - 1))

# 벽의 정보를 저장할 리스트
HORIZONTAL_WALL = 0
VERTICAL_WALL = 1

HORIZONTAL_WALL_MAP = [[False for _ in range(C)] for _ in range(R)]
VERTICAL_WALL_MAP = [[False for _ in range(C)] for _ in range(R)]

for row, col, wall_dir in WALL_INFO:
    if wall_dir == HORIZONTAL_WALL:
        HORIZONTAL_WALL_MAP[row - 1][col - 1] = True

    elif wall_dir == VERTICAL_WALL:
        VERTICAL_WALL_MAP[row - 1][col - 1] = True


# 벽을 체크하는 함수를 만들어야한다.
# 모든 벽은 격자를 안넘어가는지를 예외로 줘야한다.
# right_wall_check: 오른쪽에 벽이 있다 -> 현재 위치에 수직 벽이 존재
# left_wall_check: 왼쪽에 벽이 있다 -> 왼쪽 위치에 수직 벽이 존재
# up_wall_check:  위에 벽이 있다 -> 현재 위치에 수평 벽이 존재
# down_wall_check:  아래에 벽이 있다 -> 아래 위치에 수평 벽이 존재

def right_wall_check(r, c, direction):
    if VERTICAL_WALL_MAP[r][c]:
        return False

    new_r = r + DIRECTIONS[direction][0]
    new_c = c + DIRECTIONS[direction][1]

    if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
        return False

    return True


def left_wall_check(r, c, direction):
    new_r = r + DIRECTIONS[direction][0]
    new_c = c + DIRECTIONS[direction][1]

    if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
        return False

    if VERTICAL_WALL_MAP[new_r][new_c]:
        return False

    return True


def up_wall_check(r, c, direction):
    if HORIZONTAL_WALL_MAP[r][c]:
        return False

    new_r = r + DIRECTIONS[direction][0]
    new_c = c + DIRECTIONS[direction][1]

    if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
        return False

    return True


def down_wall_check(r, c, direction):
    new_r = r + DIRECTIONS[direction][0]
    new_c = c + DIRECTIONS[direction][1]

    if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
        return False

    if HORIZONTAL_WALL_MAP[new_r][new_c]:
        return False

    return True


def solution():
    global HORIZONTAL_WALL_MAP, VERTICAL_WALL_MAP, HEATERS, CHECK_AREA, MAP, R, C

    choco_cnt = 0
    total_heat_map = [[0] * C for _ in range(R)]

    while True:

        choco_cnt += 1
        if choco_cnt > 100:
            break

        # 1. 온품기가 바람을 방출, 각 히터 별로 발출한 열들의 좌표를 구하고 그들을 종합함.
        for h_r, h_c, h_d in HEATERS:

            curr_heat_map = [[0] * C for _ in range(R)]

            queue = collections.deque()
            new_r = h_r + DIRECTIONS[h_d][0]
            new_c = h_c + DIRECTIONS[h_d][1]

            # 온풍기는 항상 바로 벽을 보지않는다, 벽 체크 안해도 됨
            curr_heat_map[new_r][new_c] = 5

            if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
                continue

            queue.append([new_r, new_c, curr_heat_map[new_r][new_c]])

            while queue:
                curr_r, curr_c, heat = queue.popleft()

                # 남은 heat값이 0이 되었을때 더 이상 heat를 그릴 필요 없음
                if heat < 1:
                    break

                # 히터가 오른쪽으로 쏠 때 위쪽 대각, 오른쪽, 아래쪽 대각을 쏴야함
                # 1. 위쪽 대각은 현재 위치에서 위와 위쪽 칸의 오른쪽 벽이 없으면 진행가능
                # 2. 오른쪽은 현재 위치에서 오른쪽에 벽이 있으면 쏘기 가능
                # 3. 아래쪽 대각은 현재 위치에서 아래와 아래쪽 칸의 오른쪽 벽이 없으면 진행 가능
                if h_d == 0:
                    if up_wall_check(curr_r, curr_c, 2):
                        if right_wall_check(curr_r - 1, curr_c, h_d):
                            queue.append([curr_r - 1, curr_c + 1, heat - 1])
                            curr_heat_map[curr_r - 1][curr_c + 1] = heat - 1

                    if right_wall_check(curr_r, curr_c, h_d):
                        queue.append([curr_r, curr_c + 1, heat - 1])
                        curr_heat_map[curr_r][curr_c + 1] = heat - 1

                    if down_wall_check(curr_r, curr_c, 3):
                        if right_wall_check(curr_r + 1, curr_c, h_d):
                            queue.append([curr_r + 1, curr_c + 1, heat - 1])
                            curr_heat_map[curr_r + 1][curr_c + 1] = heat - 1

                # 왼쪽
                elif h_d == 1:
                    if up_wall_check(curr_r, curr_c, 2):
                        if left_wall_check(curr_r - 1, curr_c, h_d):
                            queue.append([curr_r - 1, curr_c - 1, heat - 1])
                            curr_heat_map[curr_r - 1][curr_c - 1] = heat - 1

                    if left_wall_check(curr_r, curr_c, h_d):
                        queue.append([curr_r, curr_c - 1, heat - 1])
                        curr_heat_map[curr_r][curr_c - 1] = heat - 1

                    if down_wall_check(curr_r, curr_c, 3):
                        if left_wall_check(curr_r + 1, curr_c, h_d):
                            queue.append([curr_r + 1, curr_c - 1, heat - 1])
                            curr_heat_map[curr_r + 1][curr_c - 1] = heat - 1
                # 위쪽
                elif h_d == 2:
                    if left_wall_check(curr_r, curr_c, 1):
                        if up_wall_check(curr_r, curr_c - 1, h_d):
                            queue.append([curr_r - 1, curr_c - 1, heat - 1])
                            curr_heat_map[curr_r - 1][curr_c - 1] = heat - 1

                    if up_wall_check(curr_r, curr_c, h_d):
                        queue.append([curr_r - 1, curr_c, heat - 1])
                        curr_heat_map[curr_r - 1][curr_c] = heat - 1

                    if right_wall_check(curr_r, curr_c, 0):
                        if up_wall_check(curr_r, curr_c + 1, h_d):
                            queue.append([curr_r - 1, curr_c + 1, heat - 1])
                            curr_heat_map[curr_r - 1][curr_c + 1] = heat - 1

                # 아래쪽
                elif h_d == 3:
                    if left_wall_check(curr_r, curr_c, 1):
                        if down_wall_check(curr_r, curr_c - 1, h_d):
                            queue.append([curr_r + 1, curr_c - 1, heat - 1])
                            curr_heat_map[curr_r + 1][curr_c - 1] = heat - 1

                    if down_wall_check(curr_r, curr_c, h_d):
                        queue.append([curr_r + 1, curr_c, heat - 1])
                        curr_heat_map[curr_r + 1][curr_c] = heat - 1

                    if right_wall_check(curr_r, curr_c, 0):
                        if down_wall_check(curr_r, curr_c + 1, h_d):
                            queue.append([curr_r + 1, curr_c + 1, heat - 1])
                            curr_heat_map[curr_r + 1][curr_c + 1] = heat - 1

            for row in range(R):
                for col in range(C):
                    total_heat_map[row][col] += curr_heat_map[row][col]

        # 남은 온기가 조정됨
        temperature_distribution_map = [[0] * C for _ in range(R)]

        for row in range(R):
            for col in range(C):

                if right_wall_check(row, col, 0):
                    heat_diff = total_heat_map[row][col] - total_heat_map[row][col + 1]
                    if heat_diff > 0:
                        ad = heat_diff // 4
                        if ad > 0:
                            temperature_distribution_map[row][col] -= ad
                            temperature_distribution_map[row][col + 1] += ad

                if left_wall_check(row, col, 1):
                    heat_diff = total_heat_map[row][col] - total_heat_map[row][col - 1]
                    if heat_diff > 0:
                        ad = heat_diff // 4
                        if ad > 0:
                            temperature_distribution_map[row][col] -= ad
                            temperature_distribution_map[row][col - 1] += ad

                if up_wall_check(row, col, 2):
                    heat_diff = total_heat_map[row][col] - total_heat_map[row - 1][col]
                    if heat_diff > 0:
                        ad = heat_diff // 4
                        if ad > 0:
                            temperature_distribution_map[row][col] -= ad
                            temperature_distribution_map[row - 1][col] += ad

                if down_wall_check(row, col, 3):
                    heat_diff = total_heat_map[row][col] - total_heat_map[row + 1][col]
                    if heat_diff > 0:
                        ad = heat_diff // 4
                        if ad > 0:
                            temperature_distribution_map[row][col] -= ad
                            temperature_distribution_map[row + 1][col] += ad

        for row in range(R):
            for col in range(C):
                total_heat_map[row][col] += temperature_distribution_map[row][col]

        # 3. 가장자리 온도가 1씩 감소
        # 1행, R행, 1열, C열, 즉 격자의 가장 끝부분의 온도들을 1씩 감소시킴

        for row in range(R):
            if total_heat_map[row][0] > 0:
                total_heat_map[row][0] -= 1
            if total_heat_map[row][C - 1] > 0:
                total_heat_map[row][C - 1] -= 1

        # 겹치면 안되니까
        for col in range(1, C - 1):
            if total_heat_map[0][col] > 0:
                total_heat_map[0][col] -= 1
            if total_heat_map[R - 1][col] > 0:
                total_heat_map[R - 1][col] -= 1

        accept_cnt = 0
        for check_area_r, check_area_c in CHECK_AREA:
            if total_heat_map[check_area_r][check_area_c] >= K:
                accept_cnt += 1

        if accept_cnt == len(CHECK_AREA):
            break

    return choco_cnt


print(solution())
