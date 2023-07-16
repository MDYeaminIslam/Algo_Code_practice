#So here we find two SUM. Find two numbers from the array and that two numbers addition match the target value provided by the user.
#Example: array = [3,2,5,-1,4,11,6,7] and target value = 10. from the array addition of 11 and -1 is same of 10.
#In this solution we'll use hash table or you can say dictionary. First delete targetsum to first number of the array.If that number match than it'll print otherwise we'll set the true value according to that value in the dictionary
# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []

array = [3,2,5,-1,4,11,6,7]
targetSum = 11
print(twoNumberSum(array,targetSum))