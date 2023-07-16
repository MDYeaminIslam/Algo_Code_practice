#Time : O(n) | Space: O(n)

def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for x in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1
    
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares