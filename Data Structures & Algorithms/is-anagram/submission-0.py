class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for char in s:
            freq[ord(char)-97]+=1
        for char in t:
            freq[ord(char)-97]-=1
        for x in freq:
            if x!=0:
                return False
        return True