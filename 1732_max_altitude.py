class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        ca = 0
        maxi = 0
        for x in gain:
            ca = ca + x
            if(ca > maxi):
                maxi = ca
            alt.append(x)
        return maxi

