def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in range(length):
        if weights[i] not in cache:
            cache[weights[i]] = i

    for i in range(length):
        target = limit - weights[i]
    
        if target in cache:
            if cache[target] == i:
                pass
            elif cache[target] > i:
                return [cache[target], i]
            else:
                return [i, cache[target]]

    return None