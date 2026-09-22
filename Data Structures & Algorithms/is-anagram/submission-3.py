class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        if(len(s)!=len(t)):
            return False
        for i in range(len(s)):
            freq[ord(s[i])-97]+=1
            freq[ord(t[i])-97]-=1
        
        for x in freq:
            if x!=0:
                return False
        return True