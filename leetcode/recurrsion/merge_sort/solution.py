def sort_array(nums):
    def merge_sort(nums):
        len_nums = len(nums)

        # Base case: split into individual elements
        if len_nums <= 1:
            return nums

        pivot = len_nums // 2

        left_list = merge_sort(nums[0: pivot])
        right_list = merge_sort(nums[pivot: len_nums])

        left_curser = right_curser = 0

        ret = []
        while len(left_list) > left_curser and len(right_list) > right_curser:
            if left_list[left_curser] < right_list[right_curser]:
                ret.append(left_list[left_curser])
                left_curser += 1
            else:
                ret.append(right_list[right_curser])
                right_curser += 1

        ret.extend(left_list[left_curser:])
        ret.extend(right_list[right_curser:])

        return ret

    return merge_sort(nums)
