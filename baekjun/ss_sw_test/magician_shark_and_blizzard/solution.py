"""
구슬은 1, 2, 3번으로 구성되어 있음


구슬 파괴:
상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음파편을 던져 그 칸에 있는 구슬을 모두 파괴
구슬이 파괴되면 빈칸이 됨, 벽에는 영향 없음

구슬 폭파:
같은 숫자의 구슬이 "4개 이상" 모여있으면 폭파함
계속해서 폭파를 진행하고 구슬이 없을 때 까지 반복함

구슬 변화:
연속하는 구슬은 하나의 그룹
하나의 그룹은 2개의 A와 B로 변
A: 그룹에 들어있는 구슬의 개수함
B: 그룹을 이루고있는 구슬의 번호수
그룹의 순서대로 1번 칸 부터 차례대로 A, B의 수서로 칸에 들어간다

1 * 폭발한 1번 구슬의 개수 + 2 * 폭발한 2번 구슬의 개수 + 3 * 폭발한 3번 구슬의 개
"""

N, M = map(int, input().split())
SPIRAL_MAP = [list(map(int, input().split())) for _ in range(N)]
MAGIC_INFO = [list(map(int, input().split())) for _ in range(M)]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
SHARK_POS_R = N // 2
SHARK_POS_C = N // 2


def destroy_cells(board, magic_dir, magic_dist):
    global SHARK_POS_R, SHARK_POS_C, SPIRAL_MAP
    for cells in range(1, magic_dist + 1):
        new_r = SHARK_POS_R + (cells * DIRECTIONS[magic_dir - 1][0])
        new_c = SHARK_POS_C + (cells * DIRECTIONS[magic_dir - 1][1])
        board[new_r][new_c] = 0


def convert_to_line(board, target_flat_list):
    spiral_path_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # 각각 2번씩 d 만큼 반향을 전환하면서 이동 하지만 마지막 루프에서는 3번 루프를 돔
    loop_cnt = 2
    direction = 0

    curr_r = SHARK_POS_R
    curr_c = SHARK_POS_C

    for dist in range(1, N):

        if dist == N - 1:
            loop_cnt = 3

        for loop in range(loop_cnt):

            for _ in range(dist):
                curr_r += spiral_path_directions[direction][0]
                curr_c += spiral_path_directions[direction][1]

                if board[curr_r][curr_c] != 0:
                    target_flat_list.append(board[curr_r][curr_c])

            direction = (direction + 1) % 4


def explode_cells(flat_list):
    point = 0
    curr_repeat_cnt = 1
    for idx in range(1, len(flat_list)):

        # 연속이 됨
        if flat_list[idx - 1] == flat_list[idx]:
            curr_repeat_cnt += 1

        else:
            if curr_repeat_cnt >= 4:
                for repeat_idx in range(1, curr_repeat_cnt + 1):
                    # 1이면 1점 2면 2점 3이면 3점
                    point += flat_list[idx - repeat_idx]

                    # 터뜨렸으면 0으로 바꿈
                    flat_list[idx - repeat_idx] = 0

            curr_repeat_cnt = 1

    # 진짜 악날하게 처음부터 끝까지 다 반복하는 edge case
    if curr_repeat_cnt >= 4:
        for repeat_idx in range(1, curr_repeat_cnt + 1):
            point += flat_list[len(flat_list) - repeat_idx]
            flat_list[len(flat_list) - repeat_idx] = 0

    return point


def transform_cells(flat_list):
    tmp_list = [0 for _ in range(N * N - 1)]
    tmp_list_idx = 0

    curr_repeat_cnt = 1
    for idx in range(1, len(flat_list)):

        if flat_list[idx - 1] == flat_list[idx]:
            curr_repeat_cnt += 1

        else:
            # flat_list 채우는것을 오버하면 걍 버린다. 이건 이 작업이 모두 끝난 후 N * N - 1 개로 슬라이싱 해도 된다.
            if tmp_list_idx < (N * N - 1):
                tmp_list[tmp_list_idx] = curr_repeat_cnt
                tmp_list_idx += 1

                tmp_list[tmp_list_idx] = flat_list[idx - 1]
                tmp_list_idx += 1

            curr_repeat_cnt = 1

    # 악독한 edge case인 flat_list가 비어있을 때와 미리 예방해줬던 N * N - 1 를 넘지 않을 때 처리 해주지 못했던 맨 마지막 구슬 변화 처리
    if len(flat_list) > 0 and tmp_list_idx < (N * N - 1):
        tmp_list[tmp_list_idx] = curr_repeat_cnt
        tmp_list_idx += 1

        tmp_list[tmp_list_idx] = flat_list[-1]
        tmp_list_idx += 1

    return tmp_list


def convert_to_spiral_map(src_flat_list, target_board):
    spiral_path_directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    # 각각 2번씩 d 만큼 반향을 전환하면서 이동 하지만 마지막 루프에서는 3번 루프를 돔
    loop_cnt = 2
    direction = 0

    curr_r = SHARK_POS_R
    curr_c = SHARK_POS_C

    flat_list_idx = 0

    for dist in range(1, N):

        if dist == N - 1:
            loop_cnt = 3

        for loop in range(loop_cnt):

            for _ in range(dist):
                curr_r += spiral_path_directions[direction][0]
                curr_c += spiral_path_directions[direction][1]

                if flat_list_idx < len(src_flat_list):
                    target_board[curr_r][curr_c] = src_flat_list[flat_list_idx]
                    flat_list_idx += 1
                else:
                    target_board[curr_r][curr_c] = 0

            direction = (direction + 1) % 4


def remove_zero(flat_list):
    return [num for num in flat_list if num != 0]


def solution():
    global N, M, SPIRAL_MAP, MAGIC_INFO

    ret = 0
    for magic_dir, magic_dist in MAGIC_INFO:

        flat_list = []

        # 1. 구슬 파괴
        destroy_cells(SPIRAL_MAP, magic_dir, magic_dist)

        # 한줄로 바꿔서 연속된 순서의 같은 구슬을 터뜨리기 용이하게 바꿈
        convert_to_line(SPIRAL_MAP, flat_list)

        # 2. 구슬 폭파

        while True:
            # 더 이상 터뜨릴 구슬이 없을 때까지 계속해서 반복
            point = explode_cells(flat_list)
            if point == 0:
                break
            ret += point

            # 과정중에는 계속해서 0을 삭제
            flat_list = remove_zero(flat_list)

        # 마지막에 못 터뜨린 0을 삭제
        flat_list = remove_zero(flat_list)

        # 3. 구슬 변화
        # 마무리로 문제에서 말한 변환 방식으로 구슬을 변화시킴
        flat_list = transform_cells(flat_list)

        convert_to_spiral_map(flat_list, SPIRAL_MAP)

    return ret


print(solution())
