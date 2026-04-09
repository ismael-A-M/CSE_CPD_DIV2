class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=0
        for i in range(len(nums)):
            for z in range(len(nums)):
                if z==i:
                    continue
                elif abs(nums[z]-nums[i])==k:
                    n+=1
        return(n//2)