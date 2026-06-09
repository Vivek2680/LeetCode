'''
Finding the sum of a pair that is euqal to target sum 
'''
from typing import List
'''
imports list from python lib 
for type hints
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        return and store in dict i.e. seen
        it return the two number that sum up to target
        if not then store it in seen dict
        '''
        seen ={}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement],i]
            seen[num] = i
        return []
        '''
        return empty list for the case where no pair found that there sun equal to target
        '''
obj = Solution()
print(obj.twoSum(nums=[0,1,2,3,4,5,6,7,8,9],target=10))