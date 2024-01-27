def twoSum(arr, target, n):
    # Dictionary to keep track of seen elements
    seen = {}
    # List to store pairs that add up to the target
    result = []

    # Iterate through the elements in the array
    for i in range(n):
        # Check if the complement to the current element is in the seen dictionary
        # and if it hasn't been used before (seen[target - arr[i]] == 0)
        if target - arr[i] in seen and seen[target - arr[i]] == 0:
            # Append the pair to the result list
            result.append([arr[i], target - arr[i]])
            # Mark the current element as used
            seen[arr[i]] = 1
        else:
            # Mark the current element as seen
            seen[arr[i]] = 0
    
    # If no pairs are found, append [-1, -1] to the result list
    if len(result) == 0:
        result.append([-1, -1])
    return result
