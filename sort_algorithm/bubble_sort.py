# coding: utf-8


def bubble_sort(nums):
    if not nums:
        return

    length = len(nums)
    continue_flag = True
    # 循环n-1次
    for i in xrange(length - 1):
        if not continue_flag:
            break
        continue_flag = False
        # 每次需要比较前length-i个相邻元素, 所以比较length-1-i次
        for j in xrange(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                continue_flag = True

    return nums
