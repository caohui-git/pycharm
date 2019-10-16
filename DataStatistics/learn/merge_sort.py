def countSmaller( nums):
    def merge_sort(enums):
        mid = len(enums) >> 1
        if mid:
            nums1, nums2 = merge_sort(enums[:mid]), merge_sort(enums[mid:])
            i, j = 0, 0
            # from small to large sorting
            while i < len(nums1) or j < len(nums2):
                if j == len(nums2) or (i < len(nums1) and nums1[i][1] <= nums2[j][1]):
                    res[nums1[i][0]] += j
                    enums[i + j] = nums1[i]
                    i += 1
                else:
                    enums[i + j] = nums2[j]
                    j += 1
        return enums

    res = [0] * len(nums)
    a = merge_sort(list(enumerate(nums)))
    return res
print(countSmaller([5,2]))