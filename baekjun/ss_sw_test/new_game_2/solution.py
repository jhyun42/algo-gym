N, K = map(int, input().split())
BOARD_MAP = [list(map(int, input().split())) for _ in range(N)]
PIECE_INFO = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]

DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]

PIECE_MAP = [[[] for _ in range(N)] for _ in range(N)]
for p_idx, (row, col, direction) in enumerate(PIECE_INFO):
    PIECE_MAP[row][col].append([p_idx, direction])


# 현대 상태의 체스판을 저장할 수 있는 배열을 만들고
# 체스 말 들의 정보를 저장할 수 있는 배열을 만들고 연동시킨다

def turn(piece_idx):
    global PIECE_INFO, DIRECTIONS, BOARD_MAP, PIECE_MAP

    curr_y, curr_x, direction = PIECE_INFO[piece_idx]
    diff_y, diff_x = DIRECTIONS[direction]

    new_y = curr_y + diff_y
    new_x = curr_x + diff_x

    if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N or BOARD_MAP[new_y][new_x] == 2:

        if direction == 0 or direction == 2:
            direction += 1
        else:
            direction -= 1

        diff_y, diff_x = DIRECTIONS[direction]
        new_y = curr_y + diff_y
        new_x = curr_x + diff_x

        PIECE_INFO[piece_idx][2] = direction

        if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N or BOARD_MAP[new_y][new_x] == 2:
            return BOARD_MAP[curr_y][curr_x]

    # bottom 말이 무슨 말인지 파악
    bottom = -1
    curr_piece_num = len(PIECE_MAP[curr_y][curr_x])
    for p_i in range(curr_piece_num):
        if PIECE_MAP[curr_y][curr_x][p_i][0] == piece_idx:
            bottom = p_i
            break

    move = []
    for idx in range(bottom, curr_piece_num):
        move.append(PIECE_MAP[curr_y][curr_x][idx])

    # 만약 빨간 공간에 있으면?
    if BOARD_MAP[new_y][new_x] == 1:
        move = list(reversed(move))

    # 최종적으로는 이동하는 코드 구현
    for moving_piece in move:
        PIECE_MAP[new_y][new_x].append(moving_piece)
        PIECE_MAP[curr_y][curr_x].remove(moving_piece)
        i, _ = moving_piece
        PIECE_INFO[i][0] = new_y
        PIECE_INFO[i][1] = new_x
        if len(PIECE_MAP[new_y][new_x]) >= 4:
            return len(PIECE_MAP[new_y][new_x])

    return len(PIECE_MAP[new_y][new_x])


def solution():
    global N, K, BOARD_MAP, PIECE_INFO, DIRECTIONS

    loop = 0
    ret = -1

    while loop <= 1000 and ret == -1:
        loop += 1

        # 각 말들을 하나씩 움직일때 마다 한턴
        for idx in range(K):

            height = turn(idx)

            if height >= 4:
                ret = loop
                break

    return ret


print(solution())
