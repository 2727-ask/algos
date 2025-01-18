class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        curr = 0
        count = 0
        for x in range(len(nums)):
            curr = curr + nums[x]
            nums[x] = curr
            if(curr == 0):
                count = count + 1
        return count
         