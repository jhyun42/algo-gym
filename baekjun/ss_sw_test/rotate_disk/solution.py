N, M, T = map(int, input().split())
DISK_MAP = [list(map(int, input().split())) for _ in range(N)]
ROTATIONS = [list(map(int, input().split())) for _ in range(T)]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
DEL = -1


def solve(multiplier, direction, nums_to_rotate):
    global DISK_MAP

    # 1 이면 반시계 방향
    if direction == 1:
        nums_to_rotate = nums_to_rotate * -1

    disk_idx = multiplier - 1
    while disk_idx < N:
        tmp = [0 for _ in range(M)]
        for idx in range(M):
            tmp[(idx + nums_to_rotate + M) % M] = DISK_MAP[disk_idx][idx]
        DISK_MAP[disk_idx] = tmp
        disk_idx += multiplier

    # 인접하는 숫자들 -1로 만드는 부분
    is_updated = False

    check_adj_mat = [[False for _ in range(M)] for _ in range(N)]
    for row in range(N):
        for col in range(M):

            for diff_r, diff_c in DIRECTIONS:

                new_r = row + diff_r
                new_c = (col + diff_c + M) % M

                if new_r < 0 or new_r >= N:
                    continue

                if DISK_MAP[row][col] != DEL and DISK_MAP[new_r][new_c] != DEL and DISK_MAP[row][col] == \
                        DISK_MAP[new_r][new_c]:
                    is_updated = True
                    check_adj_mat[row][col] = True
                    check_adj_mat[new_r][new_c] = True

    if is_updated:
        for row in range(N):
            for col in range(M):
                if check_adj_mat[row][col]:
                    DISK_MAP[row][col] = DEL

    else:
        # 평균값을 구해서 처리
        total_sum = 0
        total_count = 0
        for row in range(N):
            for col in range(M):
                if DISK_MAP[row][col] != DEL:
                    total_sum += DISK_MAP[row][col]
                    total_count += 1

        for row in range(N):
            for col in range(M):
                if DISK_MAP[row][col] != DEL:
                    if DISK_MAP[row][col] * total_count > total_sum:
                        DISK_MAP[row][col] -= 1
                    elif DISK_MAP[row][col] * total_count < total_sum:
                        DISK_MAP[row][col] += 1


def solution():
    global N, M, T, DISK_MAP, ROTATIONS

    for x, d, k in ROTATIONS:
        solve(x, d, k)

    ret = 0
    for row in range(N):
        for col in range(M):
            if DISK_MAP[row][col] != DEL:
                ret += DISK_MAP[row][col]

    return ret


print(solution())
