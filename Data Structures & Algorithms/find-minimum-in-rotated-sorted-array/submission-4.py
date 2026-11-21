class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        # bin search variation: what I know there are 2 sorted pieces want to find the beginning of the 2nd part. edge case if it is sorted taken care of so now it is sorted from 0:k where k<n-1
        # bin search except if it breaks we update? start at middle if it is less than start

        lo = 1
        hi = n-1
        ans = nums[0]
        while(lo<=hi):
            if nums[lo]<nums[hi]:
                return min(nums[lo],ans)
            mid = lo +(hi-lo)//2
            print(nums[lo],nums[mid],nums[hi])
            
        
            ans = min(ans,nums[mid])
            if nums[mid] >= nums[lo]:
                lo = mid +1
            else:
                hi = mid-1
        return ans