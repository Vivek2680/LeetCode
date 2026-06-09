class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen ={}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
        return []
obj = Solution()
print(obj.twoSum([0,1,2,3,4,5,6,7,8,9],10))
    
        


        