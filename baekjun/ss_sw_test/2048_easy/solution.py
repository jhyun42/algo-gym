import sys

inputs = sys.stdin.readline

N = int(inputs())
input_map = [list(map(int, inputs().split())) for _ in range(N)]


class Board(object):
    def __init__(self, in_map, n):
        self.n = n
        self.map = in_map

    def rotate(self):
        tmp = [[0] * self.n for _ in range(self.n)]
        for row_idx in range(self.n):
            for col_idx in range(self.n):
                tmp[row_idx][col_idx] = self.map[self.n - col_idx - 1][row_idx]
        self.map = tmp

    def get_max(self):
        return max(map(max, self.map))

    def move_up(self):

        tmp = [[0] * self.n for _ in range(self.n)]

        for col in range(self.n):
            flag = False
            target = -1
            for row in range(self.n):

                if self.map[row][col] == 0:
                    continue

                if flag and self.map[row][col] == tmp[target][col]:
                    tmp[target][col] *= 2
                    flag = False

                else:
                    target += 1
                    tmp[target][col] = self.map[row][col]
                    flag = True

            for t in range(target + 1, self.n):
                tmp[t][col] = 0

        self.map = tmp


def solution(n, in_map):
    ret = 0

    def dfs(curr_move_cnt, curr_board):
        nonlocal ret

        if curr_move_cnt == 5:
            curr_max = curr_board.get_max()
            ret = max(ret, curr_max)
            return

        for _ in range(4):
            next_board = Board(in_map=curr_board.map, n=curr_board.n)
            next_board.move_up()
            dfs(curr_move_cnt=curr_move_cnt + 1, curr_board=next_board)
            curr_board.rotate()

    board = Board(in_map=in_map, n=n)
    dfs(curr_move_cnt=0, curr_board=board)

    return ret


ret = solution(N, input_map)
print(ret)
