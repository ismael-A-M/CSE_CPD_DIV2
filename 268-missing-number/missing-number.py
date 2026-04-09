class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr=sorted(nums)
        c=len(arr)
        for i in range(len(arr)):
            if arr[i]!=i:
                c=i
                break
        return(c)
