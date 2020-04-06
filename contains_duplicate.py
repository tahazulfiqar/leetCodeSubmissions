class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dup_dict = {}
        
        for item in nums:
            if item in dup_dict:
                return True 
            dup_dict[item] = 1
        
        return False