def search_matrix(matrix, target):
    if not matrix:
        return False

    mat = matrix
    tg = target

    def search_rec(left, right, up, down):

        nonlocal mat
        nonlocal tg

        if left > right or up > down:
            return False

        elif tg > mat[down][right] or tg < mat[up][left]:
            return False

        mid = left + (right - left) // 2

        row = up
        while row <= down and mat[row][mid] <= tg:
            if mat[row][mid] == tg:
                return True

            row += 1

        return search_rec(left, mid - 1, row, down) or search_rec(mid + 1, right, up, row - 1)

    return search_rec(0, len(mat[0]) - 1, 0, len(mat) - 1)
