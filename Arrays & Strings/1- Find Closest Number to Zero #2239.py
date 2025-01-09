from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num2zero = nums[0]
        for x in nums:
            if abs(x) < abs(num2zero):
                num2zero = x
            if num2zero > 0 and abs(num2zero) in nums:
                return abs(num2zero)
            else:
                return num2zero