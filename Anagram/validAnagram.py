# 8.11.2023 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

# Solution 1
# creating own sorted array 
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True
    
# SOultion 2 
# 0(1) memory 
# wont work in interiew 
        # return Counter(s) == Counter(t)

# Solution 3
# using sorted function 
        # return sorted(s) == sorted(t)
