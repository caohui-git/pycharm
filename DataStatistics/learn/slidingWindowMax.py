from collections import deque
def maxSlidingWindow(nums, k: int):
    if not nums:
        return []
    q = deque()
    l = len(nums)
    ans = []
    for i in range(k):
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)

    for i in range(k, l):
        ans.append(nums[q[0]])
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        if q and i - q[0] >= k:
            q.popleft()
        q.append(i)
    ans.append(nums[q[0]])
    return ans

print(maxSlidingWindow([7,2,4],2))