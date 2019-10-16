def longestConsecutive(nums) -> int:
    hashmap = {}
    # centre explore like longest hui wen zi chuan
    lc = 0
    for i in nums:
        hashmap[i] = True
    for k in hashmap:
        if hashmap[k]:
            left = k - 1
            right = k + 1
            # hash seems to n^0.3
            while left in hashmap and hashmap[left]:
                hashmap[left] = False
                left -= 1
            while right in hashmap and hashmap[right]:
                hashmap[right] = False
                right += 1

            lc = max(lc, right - left - 1)
    return lc


print(longestConsecutive([100,4,200,1,3,2]))