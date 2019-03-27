# coding: utf-8


def selection_sort(nums):
    if not nums:
        return

    length = len(nums)
    for i in xrange(length - 1):
        min_value = nums[i]
        min_index = i
        for j in xrange(i + 1, length):
            if nums[j] < min_value:
                min_index = j
                min_value = nums[j]

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
