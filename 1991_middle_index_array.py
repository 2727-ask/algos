class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return 0
        pre = []
        post = []

        preSum = 0
        postSum = 0
        for x in nums:
            preSum = preSum + x
            pre.append(preSum)
            
        
        for x in nums[::-1]:
            postSum = postSum + x 
            post.append(postSum)

        post = post[::-1]
        
        for x in range(len(post)):
            if(post[x] == pre[x]):
                return x

        return -1    

