from typing import List


def find_numbers(nums: List[int]) -> int:
    num_even = 0
    for num in nums:

        digits_cnt = 1

        while num >= 10:
            digits_cnt += 1
            num //= 10

        if digits_cnt % 2 == 0:
            num_even += 1

    return num_even
