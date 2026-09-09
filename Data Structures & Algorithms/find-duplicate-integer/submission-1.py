class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 1 3 4 2 2 -> 4
        ## n = 4
        ## 1 2 2 2 2 2 -> 5
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1