N = int(input())
LINES = [list(map(int, input().split())) for _ in range(N)]

BOARD = [[[0 for _ in range(4)] for _ in range(10)] for _ in range(2)]

BLUE = 0
GREEN = 1

SCORE = 0
COUNT = 0


def move_point(y, x, area_color):
    global BOARD

    label = BOARD[area_color][y][x]

    BOARD[area_color][y][x] = 0

    while y < 10:
        if BOARD[area_color][y][x] != 0:
            break
        y += 1
    y -= 1

    BOARD[area_color][y][x] = label


def move_h_block(y, x, area_color):
    global BOARD

    label = BOARD[area_color][y][x]

    BOARD[area_color][y][x] = 0
    BOARD[area_color][y - 1][x] = 0

    while y < 10:
        if BOARD[area_color][y][x] != 0:
            break
        y += 1
    y -= 1

    BOARD[area_color][y][x] = label
    BOARD[area_color][y - 1][x] = label


def move_w_block(y, x, area_color):
    global BOARD

    label = BOARD[area_color][y][x]

    BOARD[area_color][y][x] = 0
    BOARD[area_color][y][x + 1] = 0

    while y < 10:
        if BOARD[area_color][y][x] != 0 or BOARD[area_color][y][x + 1] != 0:
            break
        y += 1
    y -= 1

    BOARD[area_color][y][x] = label
    BOARD[area_color][y][x + 1] = label


def remove(y, area_color):
    global BOARD
    for x in range(4):
        BOARD[area_color][y][x] = 0


def move(start_y, area_color):
    global BOARD

    for y in range(start_y, 4, -1):
        for x in range(4):
            if BOARD[area_color][y][x] == 0:
                continue
            BOARD[area_color][y + 1][x] = BOARD[area_color][y][x]
            BOARD[area_color][y][x] = 0


def delete_filled_block(area_color):
    global SCORE, BOARD

    is_remove = False

    for y in range(6, 10):

        count = 0

        for x in range(4):
            if BOARD[area_color][y][x] != 0:
                count += 1

        if count == 4:
            is_remove = True
            SCORE += 1
            remove(y, area_color)
            move(y - 1, area_color)

    if is_remove:
        delete_filled_block(area_color)


def delete_overflow_block(area_color):
    remove_count = 0

    for y in range(4, 6):

        block_exists = False

        for x in range(4):
            if BOARD[area_color][y][x] != 0:
                block_exists = True
                break

        if block_exists:
            remove_count += 1

    if remove_count > 0:
        for y in reversed(range(6, 10)):
            for x in range(4):
                BOARD[area_color][y][x] = BOARD[area_color][y - remove_count][x]

        for y in range(4, 6):
            for x in range(4):
                BOARD[area_color][y][x] = 0


def put_blocks(block_type, target, area_color, label):
    if block_type == 1:
        BOARD[area_color][0][target] = label
        move_point(0, target, area_color)

    elif (block_type == 2 and area_color == BLUE) or (block_type == 3 and area_color == GREEN):
        BOARD[area_color][0][target] = label
        BOARD[area_color][1][target] = label
        move_h_block(1, target, area_color)

    elif (block_type == 3 and area_color == BLUE) or (block_type == 2 and area_color == GREEN):
        BOARD[area_color][0][target] = label
        BOARD[area_color][0][target + 1] = label
        move_w_block(0, target, area_color)

    # 빈 라인이 있으면 채우고
    delete_filled_block(area_color)

    # 꽉 찬 블록이 있으면 지우고
    delete_overflow_block(area_color)


def solution():
    global COUNT, BLUE, GREEN

    for idx, (block_type, y, x) in enumerate(LINES):
        put_blocks(block_type, y, BLUE, idx + 1)
        put_blocks(block_type, x, GREEN, idx + 1)

    # 남은 블럭 개수 세
    for color in range(2):
        for y in range(4, 10):
            for x in range(4):
                if BOARD[color][y][x] != 0:
                    COUNT += 1


solution()
print(SCORE)
print(COUNT)
