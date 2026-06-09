class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        heights.append(0)

        for i in range(len(heights)):

            while stack and heights[stack[-1]] > heights[i]:

                h = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1

                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea