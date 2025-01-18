class Solution:
    def maxScore(self, s: str) -> int:
        prefix = []
        postfix = []
        zeros = 0 
        ones = 0
        maxi = 0
        for x in range(len(s)):
            if(s[x] == "0"):
                zeros = zeros + 1 
                prefix.append(zeros)
            else:
                prefix.append(zeros) 
     
        for x in range(len(s)-1, 0, -1):
            if(s[x] == "1"):
                ones = ones + 1
                postfix.append(ones)
            else:
                postfix.append(ones)    
        print(prefix, postfix[::-1])

        curr = 0
        postfix = postfix[::-1]
        for x in range(len(prefix)-1):
           curr = prefix[x] + postfix[x] 
           maxi = max(curr, maxi)
        return maxi   