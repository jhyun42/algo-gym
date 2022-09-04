def sorted_squares_1(nums):
    return sorted(x * x for x in nums)


def sorted_squares_2(nums):
    num_nums = len(nums)

    result_list = [0] * num_nums

    left = 0
    right = num_nums - 1

    for i in range(num_nums - 1, -1, -1):

        if abs(nums[left]) < abs(nums[right]):
            square = nums[right]
            right -= 1

        else:
            square = nums[left]
            left += 1

        result_list[i] = square * square

    return result_list
