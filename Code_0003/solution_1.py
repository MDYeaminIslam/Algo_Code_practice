#Time: O(nlogn) | Space: O(n)

def sortedSquaredArray(array):
    # Write your code here.
    sortedSquares = [0 for x in array]
    
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value
        
    sortedSquares.sort()
    return sortedSquares

array = [-5,-3,-4,0,3,5,8]
print(sortedSquaredArray(array))