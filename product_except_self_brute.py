class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        i = 0
        j = 0
        product = 1
        
        while j<len(nums):
            
            if j != i:
                product *= nums[i]
            
            i+=1
            
            if i == len(nums):
                j+=1
                result.append(product)
                product = 1
                i = 0
        
        return result