class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        result[0] = 1
        right_product = 1
                        
        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right_product *= nums[i+1]
            result[i] *= right_product
            
        return result