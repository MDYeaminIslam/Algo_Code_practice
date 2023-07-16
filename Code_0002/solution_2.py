#Find the Subsequence of the array.
#Example: array = [1,0,-7,8,9,2,1] and subsequence = [0,8,2,1]
# Time: O(n) | Space: O(1)
def isValidSubsequence(array, sequence):
    subarrID = 0
    for value in array:
        if subarrID == len(sequence):
            break
        if sequence[subarrID] == value:
            subarrID += 1
    return subarrID == len(sequence)
    
    
array = [1,0,-7,8,9,2,1]
sequence = [0,8,2,1]
print(isValidSubsequence(array,sequence))
