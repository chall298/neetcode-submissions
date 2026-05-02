class Solution:
    def trap(self, height: List[int]) -> int:
        
        # res = 0
        # l, r = 0, len(height) - 1

        # while l < r:
        #     area = (r - l) * min(height[l], height[r])
        #     res = max(res, area)

        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return res

        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else: 
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res