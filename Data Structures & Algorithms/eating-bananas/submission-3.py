class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        if h < n:
            return False
        if n == 1:
            return math.ceil(piles[0]/h)

        min_k = max(piles)
        # find_k =[i+1 for i in range(min_k)]

        lo,hi = 0,min_k-1
        mid = lo + (hi-lo)//2

        while lo <= hi:
            mid = lo+(hi-lo)//2
            num_hours= sum(math.ceil(x/mid) for x in piles)
            # for x in piles:
            #     num_hours += math.ceil(x/mid) 
            if num_hours > h:
                lo = mid+1
            elif num_hours <= h:
                min_k = min(mid,min_k)
                hi = mid-1
            
        return min_k

