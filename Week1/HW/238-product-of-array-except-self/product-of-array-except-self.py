class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre, post = 1, 1
        output = []
        for i in range(n):
            output.append(pre)
            pre *=  nums[i]
        for i in range (n-1, -1, -1):
            output[i] *= post
            post *=  nums[i]
        return output
        


        