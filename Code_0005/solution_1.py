# Time: O(nlogn) | Space: O(1)

def nonConstructibleChange(coins):
    coins.sort()
    
    currentChangeCreated = 0
    
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated
        currentChangeCreated += coin
        
    return currentChangeCreated

coins = [5,7,1,1,2,3,22]
makeBillOf = 20

if(nonConstructibleChange(coins) >= makeBillOf):
    print("You can make bill of " + str(makeBillOf) + " with given coins")
else:
    print("You can't make bill of " + str(makeBillOf) + " with given coins")