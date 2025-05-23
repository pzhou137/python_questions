def get_max_cost(s: str) -> int:
    """
    Calculate the maximum cost of transforming a binary string by moving '1's to the right.
    Each move of a '1' to an adjacent position costs 1 plus the number of positions moved.
    
    Args:
        s (str): A binary string containing '0's and '1's
        
    Returns:
        int: The maximum possible cost of moving all '1's to the rightmost positions
    """
    # Get the length of the input string
    n = len(s)
    
    # Create a list of positions where '1's are located in the input string
    positions = [i for i in range(n) if s[i] == '1']

    if not positions:
        return 0
    
    max_cost = 0
    
    # First phase: Process '1's from right to left, moving them as far right as possible
    # while maintaining their relative order
    for i in range(len(positions) - 1, 0, -1):
        # Check if there's a gap between consecutive '1's
        if positions[i] - positions[i-1] > 1:
            # Calculate the cost of moving the '1' to the right
            cost = positions[i] - positions[i-1]
            # Add cost to total
            max_cost += cost
            # Update the position of the '1' that was moved
            positions[i-1] = positions[i] - 1
    
    # Second phase: Move all '1's to the rightmost positions
    # Start from the rightmost position of the string
    final_position = n - 1
    for x in positions:
        # Calculate the cost of moving the '1' to the right
        cost = final_position - x + 1
        # Add cost to total
        max_cost += cost
        # Update the next available rightmost position
        final_position -= 1
    
    return max_cost

if __name__ == "__main__":
    s = "110100"
    s2 = "10010100"
    print(get_max_cost(s2))

            