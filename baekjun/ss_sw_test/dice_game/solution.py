DICE_POSSIBLES = list(map(int, input().split()))

BOARD_SCORE = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 13, 16, 19, 25,
    30, 35, 22, 24, 28,
    27, 26, 0
]

TO_GO_LOOKUP = [
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
    [5, 6, 7, 8, 9],
    [21, 22, 23, 24, 25],
    [7, 8, 9, 10, 11],
    [8, 9, 10, 11, 12],
    [9, 10, 11, 12, 13],
    [10, 11, 12, 13, 14],
    [27, 28, 24, 25, 26],
    [12, 13, 14, 15, 16],
    [13, 14, 15, 16, 17],
    [14, 15, 16, 17, 18],
    [15, 16, 17, 18, 19],
    [29, 30, 31, 24, 25],
    [17, 18, 19, 20, 32],
    [18, 19, 20, 32, 32],
    [19, 20, 32, 32, 32],
    [20, 32, 32, 32, 32],
    [32, 32, 32, 32, 32],
    [22, 23, 24, 25, 26],
    [23, 24, 25, 26, 20],
    [24, 25, 26, 20, 32],
    [25, 26, 20, 32, 32],
    [26, 20, 32, 32, 32],
    [20, 32, 32, 32, 32],
    [28, 24, 25, 26, 20],
    [24, 25, 26, 20, 32],
    [30, 31, 24, 25, 26],
    [31, 24, 25, 26, 20],
    [24, 25, 26, 20, 32],
    [32, 32, 32, 32, 32]
]


def get_score(state):
    global BOARD_SCORE, TO_GO_LOOKUP

    ret = 0
    visited = [False] * len(BOARD_SCORE)
    four_piece_pos = [0] * 4

    for idx, piece_to_move in enumerate(state):
        move = DICE_POSSIBLES[idx] - 1
        curr_pos = four_piece_pos[piece_to_move]
        next_pos = TO_GO_LOOKUP[curr_pos][move]
        add_score = BOARD_SCORE[next_pos]

        if visited[next_pos] and next_pos != 32:
            return -1

        ret += add_score
        visited[curr_pos] = False
        visited[next_pos] = True

        four_piece_pos[piece_to_move] = next_pos

    return ret


def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next_perm in permutations(array, r - 1):
                yield [array[i]] + next_perm


def solution():
    global DICE_POSSIBLES, CELLS, TO_GO_LOOKUP

    ret = 0

    for perm in permutations(list(range(4)), 10):
        candi = get_score(perm)
        ret = max(candi, ret)

    return ret


print(solution())
