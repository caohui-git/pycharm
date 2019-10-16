def maxProduct(nums):
    n = len(nums)
    if n == 0:
        return None
    # 每一次运算记录最大值和最小值，最小值放在第一位，最大值放在第二位
    record = [[0, 0] for i in range(n)]
    # 初始化第一个记录
    record[0][0], record[0][1] = nums[0], nums[0]
    max_value = nums[0]
    # 从第二个元素开始计算
    index = 1
    while index < n:
        # 一个可能的最值（最大最小不知）
        t1 = record[index - 1][0] * nums[index]
        # 另一个可能的最值（最大最小不知）
        t2 = record[index - 1][1] * nums[index]
        # 最小值
        record[index][0] = min(nums[index], t1, t2)
        # 最大值
        record[index][1] = max(nums[index], t1, t2)
        # 最大值比较函数
        max_value = max(record[index][1], max_value)
        index += 1
    return max_value
t=maxProduct([2,3,-2,4])
print(t)