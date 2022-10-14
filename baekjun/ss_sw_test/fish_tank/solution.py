N, K = map(int, input().split())
FISH_TANK = list(map(int, input().split()))
NO_VALUE = -1
MAX_BOARD_SIZE = 101

DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def search_min_and_add(array):
    min_value = 10000
    min_value_indices = []

    for idx in range(len(array)):

        if array[idx] < min_value:
            min_value = array[idx]
            min_value_indices = [idx]

        elif min_value == array[idx]:
            min_value_indices.append(idx)

    for idx in min_value_indices:
        array[idx] += 1


def roll_stack(board):
    stack_start = 0
    stack_width = 1
    stack_height = 1

    while stack_start + stack_height + stack_width <= N:

        for row in range(stack_height):
            for col in range(stack_width):
                new_y = stack_width - col
                new_x = stack_start + stack_width + row
                board[new_y][new_x] = board[row][col + stack_start]
                board[row][col + stack_start] = NO_VALUE

        stack_start += stack_width
        if stack_height == stack_width:
            stack_height += 1
        else:
            stack_width += 1


def distribute_fishes(board):
    tmp_board = [[NO_VALUE for _ in range(MAX_BOARD_SIZE)] for _ in range(MAX_BOARD_SIZE)]
    for row in range(MAX_BOARD_SIZE):
        for col in range(MAX_BOARD_SIZE):
            tmp_board[row][col] = board[row][col]

    for row in range(N):
        for col in range(N):

            if board[row][col] == NO_VALUE:
                continue

            for diff_r, diff_c in DIRECTION:

                new_r = diff_r + row
                new_c = diff_c + col

                if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N or board[new_r][new_c] == NO_VALUE:
                    continue

                tmp_board[row][col] += int((board[new_r][new_c] - board[row][col]) / 5)

    flat_tank = []
    for col in range(N):
        for row in range(N):
            if tmp_board[row][col] == -1:
                continue
            else:
                flat_tank.append(tmp_board[row][col])

    tmp_board = [[NO_VALUE for _ in range(MAX_BOARD_SIZE)] for _ in range(MAX_BOARD_SIZE)]
    for col in range(N):
        tmp_board[0][col] = flat_tank[col]

    for row in range(MAX_BOARD_SIZE):
        for col in range(MAX_BOARD_SIZE):
            board[row][col] = tmp_board[row][col]


def fold_tanks(board):
    stack_start = 0
    stack_height = 1
    mid = N // 2

    # 상어 새끼 두번 뻘짓함
    for _ in range(2):

        for row in range(stack_height):
            for col in range(mid):
                new_r = 2 * stack_height - row - 1
                new_c = 2 * mid + stack_start - col - 1
                board[new_r][new_c] = board[row][col + stack_start]
                board[row][col + stack_start] = -1
        stack_start += mid
        mid //= 2
        stack_height *= 2


def solution():
    fish_tank = FISH_TANK

    ret = 0
    while not (max(fish_tank) - min(fish_tank)) <= K:
        ret += 1

        # 1. 최소 값에 물고기 넣음
        search_min_and_add(fish_tank)

        # 일단 각종 위치변환 연산에 용이하게 matrix 형태로 변환
        tmp_board = [[NO_VALUE for _ in range(MAX_BOARD_SIZE)] for _ in range(MAX_BOARD_SIZE)]
        for col in range(N):
            tmp_board[0][col] = fish_tank[col]

        # 2. 왼쪽 어항을 말듯이 쌓음
        roll_stack(tmp_board)

        # 3. 물고기 이동
        distribute_fishes(tmp_board)

        # 4. 두번 접기
        fold_tanks(tmp_board)

        # 5. 다시 물고기 이동
        distribute_fishes(tmp_board)

        fish_tank = [NO_VALUE for _ in range(N)]
        for col in range(N):
            fish_tank[col] = tmp_board[0][col]

    return ret


print(solution())
