# coding: utf-8


def insertion_sort(nums):
    if not nums:
        return

    length = len(nums)
    # 从第1个数开始排序(第0个默认有序)
    for i in xrange(1, length):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums
