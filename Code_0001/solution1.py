#So here we find two SUM. Find two numbers from the array and that two numbers addition match the target value provided by the user.
#Example: array = [3,2,5,-1,4,11,6,7] and target value = 10. from the array addition of 11 and -1 is same of 10.
#In solution 1 we'll use two for loop. In first loop we'll take first array number and in second array we'll start addition first number with 2nd number to last number of the array and check if the addition match the target number.
#Here Complexity:- Time=O(n^2) | Space=O(1)

def twoNumberSum(array,targetSum):
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1,len(array)-1):
            secondNum = array[j]
            if firstNum+secondNum == targetSum:
                return [firstNum,secondNum]
    return []

array = [3,2,5,-1,4,11,6,7]
targetSum = 10
print(twoNumberSum(array,targetSum))