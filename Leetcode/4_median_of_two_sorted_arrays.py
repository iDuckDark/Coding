def find_median_sorted_arrays(nums1, nums2):
    ls = nums1 + nums2
    ls.sort()
    print(ls)
    i = len(ls) / 2
    if len(ls) % 2 == 0:
        return (ls[i - 1] + ls[i]) / 2
    return ls[int((len(ls) + 1) / 2) - 1]


def test_find_median_sorted_arrays():
    nums1 = [1, 3]
    nums2 = [2]
    # expected = 2.0
    find_median_sorted_arrays(nums1, nums2)


def main():
    test_find_median_sorted_arrays()


main()
