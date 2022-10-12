R, C, M = map(int, input().split())
SHARKS = [list(map(int, input().split())) for _ in range(M)]


def catch_shark(fishing_map, fisher_king_pos):
    global R, C, M

    caught_shark_weight = 0
    for r in range(R):
        if fishing_map[r][fisher_king_pos][2] != 0:
            caught_shark = fishing_map[r][fisher_king_pos]
            fishing_map[r][fisher_king_pos] = [0, 0, 0]
            caught_shark_weight = caught_shark[2]
            break
    return caught_shark_weight


# direction = 1 -> up
# direction = 2 -> down
# direction = 3 -> right
# direction = 4 -> left
def move_sharks(fishing_map):
    global R, C, M, SHARKS
    tmp_fishing_map = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]

    for row in range(R):
        for col in range(C):
            if fishing_map[row][col][2] != 0:

                s, d, z = fishing_map[row][col]

                if d == 1:
                    # y 감소
                    new_y = (((R - 1) * 2) - row) + s
                    new_y = (new_y % ((R - 1) * 2))
                    next_d = 2

                    if new_y >= (R - 1):
                        new_y = ((R - 1) * 2) - new_y
                        next_d = 1

                    tar_z = tmp_fishing_map[new_y][col][2]
                    if tar_z < z:
                        tmp_fishing_map[new_y][col] = [s, next_d, z]

                elif d == 2:
                    # y 증가
                    new_y = row + s
                    new_y = (new_y % ((R - 1) * 2))
                    next_d = 2
                    if new_y >= (R - 1):
                        new_y = ((R - 1) * 2) - new_y
                        next_d = 1

                    tar_z = tmp_fishing_map[new_y][col][2]
                    if tar_z < z:
                        tmp_fishing_map[new_y][col] = [s, next_d, z]

                elif d == 3:
                    # x 증가
                    new_x = col + s
                    new_x = (new_x % ((C - 1) * 2))
                    next_d = 3
                    if new_x >= (C - 1):
                        new_x = ((C - 1) * 2) - new_x
                        next_d = 4

                    tar_z = tmp_fishing_map[row][new_x][2]
                    if tar_z < z:
                        tmp_fishing_map[row][new_x] = [s, next_d, z]

                elif d == 4:
                    # x 감소
                    new_x = (((C - 1) * 2) - col) + s
                    new_x = (new_x % ((C - 1) * 2))
                    next_d = 3

                    if new_x >= C - 1:
                        new_x = ((C - 1) * 2) - new_x
                        next_d = 4

                    tar_z = tmp_fishing_map[row][new_x][2]
                    if tar_z < z:
                        tmp_fishing_map[row][new_x] = [s, next_d, z]

    return tmp_fishing_map


def solution():
    global R, C, M, SHARKS

    fishing_map = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]

    for shark_y, shark_x, s, d, z in SHARKS:
        fishing_map[shark_y - 1][shark_x - 1][0] = s
        fishing_map[shark_y - 1][shark_x - 1][1] = d
        fishing_map[shark_y - 1][shark_x - 1][2] = z

    ret = 0
    curr_fisher_king_pos = 0
    while curr_fisher_king_pos < C:
        # 낚시 왕이 오른쪽 한칸으로 이동함

        # 낚시왕이 있는 열에 상어중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
        ret += catch_shark(fishing_map, curr_fisher_king_pos)

        # 상어들 이동시키기
        fishing_map = move_sharks(fishing_map)

        curr_fisher_king_pos += 1

    return ret


print(solution())
