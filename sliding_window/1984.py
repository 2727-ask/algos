class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if(len(nums) == 1 or k == 1):
            return 0
        
        nums = sorted(nums)[::-1]
        mini = 9000000
        i = 0
        j = k-1
        print(nums)
        while(i < j and j < len(nums)):
            mini = min(mini, nums[i]-nums[j])
            i = i + 1
            j = j + 1
        return mini
            
        