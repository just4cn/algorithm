# coding: utf-8

import time
from random import shuffle, choice
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from selection_sort import selection_sort


def test_sort(func_list, nums):
    result = sorted(nums)
    for func in func_list:
        shuffle(nums)
        print func.__name__,
        start_time = time.time()
        assert result == func(nums)
        print time.time() - start_time


def main():
    nums = range(1000)
    sort_nums = [choice(nums) for _ in xrange(5000)]
    func_list = [bubble_sort, insertion_sort, selection_sort, merge_sort]
    test_sort(func_list, sort_nums)


if __name__ == '__main__':
    main()
