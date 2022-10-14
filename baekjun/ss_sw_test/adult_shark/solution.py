N, M, K = map(int, input().split())
SHARK_MAP = [list(map(int, input().split())) for _ in range(N)]
SHARK_DIRECTIONS = list(map(int, input().split()))
SHARK_PRIORITY = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution():
    global K

    # board idx = 0: 상어의 번호
    # board idx = 1: 번호별 상어 냄새 위치
    # board ids = 2: 상어의 냄새 강도
    board = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

    sharks = [[0, 0, 0] for _ in range(M)]

    for r in range(N):
        for c in range(N):
            board[0][r][c] = SHARK_MAP[r][c]
            if board[0][r][c] != 0:
                shark_number = board[0][r][c] - 1
                sharks[shark_number][0] = r
                sharks[shark_number][1] = c

                board[1][r][c] = board[0][r][c]
                board[2][r][c] = K

    for shark_idx, direction in enumerate(SHARK_DIRECTIONS):
        sharks[shark_idx][2] = direction - 1

    ret = -1
    time = 0
    killed_shark = 0
    while time <= 1000:
        time += 1

        tmp_board = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]

        for r in range(N):
            for c in range(N):

                # 일단 값을 복사
                tmp_board[0][r][c] = board[0][r][c]
                tmp_board[2][r][c] = board[2][r][c]

                # 만약에 냄새가 해당 위치에 있었다면 한턴 지났으니까 해당 위치의 냄새 수명 줄이고
                if tmp_board[2][r][c] > 0:
                    tmp_board[2][r][c] -= 1

                # 그래도 남아있으면 냄새 위치에 적용
                if tmp_board[2][r][c] > 0:
                    tmp_board[1][r][c] = board[1][r][c]

        # 모든 상어들 한번 씩
        for shark_idx in range(M):

            curr_y = sharks[shark_idx][0]
            curr_x = sharks[shark_idx][1]
            curr_d = sharks[shark_idx][2]

            # 상어 죽었으면 그 상어는 안봄
            if curr_y == -1:
                continue

            is_moved = False

            # 이동시켜 보자
            for dir_idx in range(4):

                # 답 안나오면 여기 디버거 찍어볼 것
                new_direction = SHARK_PRIORITY[shark_idx][curr_d][dir_idx] - 1

                new_y = curr_y + DIRECTIONS[new_direction][0]
                new_x = curr_x + DIRECTIONS[new_direction][1]

                # 해당 방향으로 이동이 가능한지
                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N or board[2][new_y][new_x] != 0:
                    continue

                is_moved = True

                # 이동했으니까 이전 위치는 꺠끗하게 치우고
                tmp_board[0][curr_y][curr_x] = 0

                # 새로운 위치에 값을 써가자
                if tmp_board[0][new_y][new_x] == 0:

                    # 상어 인덱스는 1부터 시작하니까
                    tmp_board[0][new_y][new_x] = shark_idx + 1
                    tmp_board[1][new_y][new_x] = shark_idx + 1

                    # 처음 방문하는 곳이니까 냄새가 새로움
                    tmp_board[2][new_y][new_x] = K

                    # 상어 상태판도 갱신해줘야겠지?
                    sharks[shark_idx][0] = new_y
                    sharks[shark_idx][1] = new_x
                    sharks[shark_idx][2] = new_direction

                # 만약 상어가 있었다면 더 낮은 idx의 상어가 기존상어를 잡아먹음. 그러니까 방금 막 도착한 친구가 사라진다.
                else:
                    killed_shark += 1
                    sharks[shark_idx][0] = -1

                # 한칸 이동이 가능하면 바로 이동 후 break
                break

            if not is_moved:
                for dir_idx in range(4):
                    # 답 안나오면 여기 디버거 찍어볼 것
                    new_direction = SHARK_PRIORITY[shark_idx][curr_d][dir_idx] - 1

                    new_y = curr_y + DIRECTIONS[new_direction][0]
                    new_x = curr_x + DIRECTIONS[new_direction][1]

                    # 해당 방향으로 이동이 가능한지
                    if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                        continue

                    if board[2][new_y][new_x] != 0 and board[1][new_y][new_x] != shark_idx + 1:
                        continue

                    # 이동했으니까 이전 위치는 꺠끗하게 치우고
                    tmp_board[0][curr_y][curr_x] = 0

                    # 새로운 위치에 값을 써가자
                    if tmp_board[0][new_y][new_x] == 0:

                        # 상어 인덱스는 1부터 시작하니까
                        tmp_board[0][new_y][new_x] = shark_idx + 1
                        tmp_board[1][new_y][new_x] = shark_idx + 1

                        # 처음 방문하는 곳이니까 냄새가 새로움
                        tmp_board[2][new_y][new_x] = K

                        # 상어 상태판도 갱신해줘야겠지?
                        sharks[shark_idx][0] = new_y
                        sharks[shark_idx][1] = new_x
                        sharks[shark_idx][2] = new_direction

                    # 만약 상어가 있었다면 더 낮은 idx의 상어가 기존상어를 잡아먹음. 그러니까 방금 막 도착한 친구가 사라진다.
                    else:
                        killed_shark += 1
                        sharks[shark_idx][0] = -1

                    # 한칸 이동이 가능하면 바로 이동 후 break
                    break

        # 1 빼고 모든 상어가 죽었으면 마무리
        if killed_shark == M - 1:
            break

        for row in range(N):
            for col in range(N):
                board[0][row][col] = tmp_board[0][row][col]
                board[1][row][col] = tmp_board[1][row][col]
                board[2][row][col] = tmp_board[2][row][col]

    if time <= 1000:
        ret = time

    return ret


print(solution())
