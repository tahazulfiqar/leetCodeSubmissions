class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_sum = 0
        stored_sums = []
        smallest_neg = float('-inf')
        seen_positive = False 
        
        for num in nums:
            
            running_sum += num
            
            if running_sum < 0:
                running_sum = 0
                stored_sums.append(running_sum)
                
                if num > smallest_neg:
                    smallest_neg = num
                    
                
            else:
                seen_positive = True
                stored_sums.append(running_sum)
        
        if seen_positive:        
            return max(stored_sums)
        
        else:
            return smallest_neg