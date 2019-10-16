def largestRectangleArea(heights):
    # one direction stack
    stack = []
    heights.append(0)
    res = 0
    n = len(heights)
    for i in range(n):
        # right border
        if not stack or heights[i] > heights[stack[-1]]:
            stack.append(i)
        else:
            # search left border
            while stack and heights[i] <= heights[stack[-1]]:
                h = heights[stack[-1]]
                stack.pop()
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)

    return res
print(largestRectangleArea([0,5,5,4]))