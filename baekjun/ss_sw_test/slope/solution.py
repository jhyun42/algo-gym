import sys

INPUT = sys.stdin.readline
N, L = map(int, INPUT().split())
MAP = [list(map(int, INPUT().split())) for _ in range(N)]


def solution():
    global MAP, N, L

    rotated_map = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            rotated_map[row][col] = MAP[N - col - 1][row]
    new_map = MAP + rotated_map

    ret = 0
    for row in range(2 * N):

        cnt = 1
        is_traversed = True

        for col in range(N - 1):

            if new_map[row][col] == new_map[row][col + 1]:
                cnt += 1

            elif ((new_map[row][col] + 1) == new_map[row][col + 1]) and cnt >= L:
                cnt = 1

            elif (new_map[row][col] == (new_map[row][col + 1] + 1)) and cnt >= 0:
                cnt = (1 - L)

            else:
                is_traversed = False
                break

        if is_traversed and cnt >= 0:
            ret += 1

    return ret


ret = solution()
print(ret)
