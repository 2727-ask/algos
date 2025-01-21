class Solution:
    def findLHS(self, nums: List[int]) -> int:
        i = 0 
        maxi = 0
        mapi = {}
        for x in nums:
            if(mapi.get(x) != None):
                mapi[x] = mapi[x] + 1
            else:
                mapi[x] = 1
        
        for x in mapi:
            if(mapi.get(x+1) != None):
                maxi = max(maxi, mapi.get(x+1) + mapi[x])
        return maxi

                
