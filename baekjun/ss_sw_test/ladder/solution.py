import sys

INPUT = sys.stdin.readline
N, M, H = map(int, INPUT().split())
HORIZONTAL_LINE = []
if M:
    HORIZONTAL_LINE = [list(map(int, INPUT().split())) for _ in range(M)]


def solution():
    global N, M, H

    ladder_map = [[False] * N for _ in range(H)]
    for a, b in HORIZONTAL_LINE:
        ladder_map[a - 1][b - 1] = True

    ret = 4

    def check():
        nonlocal ladder_map

        for col in range(N):
            pos = col

            for row in range(H):

                if ladder_map[row][pos]:
                    pos += 1

                elif ladder_map[row][pos - 1]:
                    pos -= 1

            if col != pos:
                return False

        return True

    def backtracking(count, y, x):

        nonlocal ret, ladder_map

        if count >= ret:
            return

        if check():
            ret = count
            return

        if count == 3:
            return

        for row in range(y, H):

            if row == y:
                k = x
            else:
                k = 0

            for col in range(k, N - 1):

                if 0 < col:
                    if ladder_map[row][col] or ladder_map[row][col - 1] or ladder_map[row][col + 1]:
                        continue

                else:
                    if ladder_map[row][col] or ladder_map[row][col + 1]:
                        continue

                ladder_map[row][col] = True
                backtracking(count + 1, row, col)
                ladder_map[row][col] = False

    backtracking(0, 0, 0)

    if ret > 3:
        return -1

    return ret


ret = solution()
print(ret)
