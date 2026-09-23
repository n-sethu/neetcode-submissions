class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkFreq(s:str)->List[int]:
            freq = [0]*26
            for x in s:
                freq[ord(x)-ord('a')]+=1
            return freq
            
        dick = defaultdict(list)
        ls=[]
        i=0
        for s in strs:
            k = checkFreq(s)
            dick[tuple(k)].append(s)
        return list(dick.values())
    

