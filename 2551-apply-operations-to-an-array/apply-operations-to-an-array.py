class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        p=[0]*len(nums)
        c=0
        for i in nums:
            if i>0:
                p[c]=i
                c+=1
        return(p)
