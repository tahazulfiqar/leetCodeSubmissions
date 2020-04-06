class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_map = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            
            if curr in result_map:
                return [result_map[curr], i]
            
            if nums[i] not in result_map:
                result_map[nums[i]] = i  
