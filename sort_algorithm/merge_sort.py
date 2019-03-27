# coding: utf-8


def merge_sort(nums):
    length = len(nums)
    if length < 2:
        return nums

    mid = length / 2

    return merge(merge_sort(nums[0:mid]), merge_sort(nums[mid:]))


def merge(nums1, nums2):
    i = j = 0
    length1, length2 = len(nums1), len(nums2)
    nums = list()
    while i < length1 and j < length2:
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1

    if i < length1:
        nums.extend(nums1[i:])
    if j < length2:
        nums.extend(nums2[j:])

    return nums
