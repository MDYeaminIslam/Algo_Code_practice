#So here we find two SUM. Find two numbers from the array and that two numbers addition match the target value provided by the user.
#Example: array = [3,2,5,-1,4,11,6,7] and target value = 10. from the array addition of 11 and -1 is same of 10.
#In this solution, first of all we sort the array increasing order.Here we take two pointer which are left pointer and right pointer. Than we'll add first value and last value. If the currentSum is smaller than targetSum than we'll increase the left pointer value and right pointer will remain same and vice versa.

# O(nlog(n)) | O(1) space

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []

array = [3,2,4]
targetSum = 6
print(twoNumberSum(array,targetSum))

"""
accepted solution from leetcode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
        return []
"""