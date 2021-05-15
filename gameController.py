# method for the computer to decide which move to take
def computer_move(state, alpha, beta, maxTurn):
    # checking for game ending states
    if (sum(state) == 1 and maxTurn) or (sum(state) == 0 and not maxTurn): return (-1, [state])
    if (sum(state) == 1 and not maxTurn) or (sum(state) == 0 and maxTurn): return (1, [state])
    
    if maxTurn:
        #set our initial bestValue to our infinity lower bound
        bestValue = -float('inf')
        result = None
        for i in find_next(state):
            # recursively search for the next possible move
            val, temp = computer_move(i, alpha, beta, not maxTurn)
            if val > bestValue:
                bestValue = val
                result = temp
            # update the upper bound
            alpha = max(alpha, val)
            #if beta and alpha have crossed, there is no result for this path, break
            if alpha >= beta:
                break
        return bestValue, [state] + result
    else:
        #set our initial bestValue to our infinity upper bound
        bestValue = float('inf')
        result = None
        for i in find_next(state):
            # recursively search for the next possible move
            val, temp = computer_move(i, alpha, beta, not maxTurn)
            if val < bestValue:
                bestValue = val
                result = temp
            beta = min(beta, val)
            #if beta and alpha have crossed, there is no result for this path, break
            if alpha >= beta:
                break
        return bestValue, [state] + result
    
# find all possible next moves
def find_next(state):
    visited = set()
    result = []
    
    for i in range(len(state)):
        for m in range(1, state[i] + 1):
            temp = list(state[:])
            temp[i] -= m
            
            # check if already exists
            rearranged = tuple(sorted(temp))
            if rearranged not in visited:
                result.append(temp)
                visited.add(rearranged)
    
    return result