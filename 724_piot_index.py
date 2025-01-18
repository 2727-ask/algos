class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre = []
        post = []
        c1 = 0
        c2 = 0
        l = len(nums)
        for x in range(l):
            c1 = c1 + nums[x]
            c2 = c2 + nums[l-x-1]
            pre.append(c1)
            post.append(c2)
        post = post[::-1]
        print(pre, post)

        for x in range(l):
            if(pre[x] == post[x]):
                return x
        return -1    




