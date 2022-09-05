def remove_element(nums, val):
    len_nums = len(nums)
    k = 0

    for idx in range(len_nums):

        if nums[idx] != val:
            nums[k] = nums[idx]
            k += 1

    return k
