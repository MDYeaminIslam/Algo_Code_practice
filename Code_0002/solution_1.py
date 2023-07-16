#Find the Subsequence of the array.
#Example: array = [1,0,-7,8,9,2,1] and subsequence = [0,8,2,1]
# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    arrID = 0
    subarrID = 0
    while arrID < len(array) and subarrID < len(sequence):
        if array[arrID] == sequence[subarrID]:
            subarrID += 1
        arrID += 1
    return subarrID == len(sequence)

array = [1,0,-7,8,9,2,1]
sequence = [0,8,2,1]
print(isValidSubsequence(array,sequence))
