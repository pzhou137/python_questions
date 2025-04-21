# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

#loop through the array, each time find the largest number and swap it with the first element
#keep track of the number of swaps
#return the number of swaps

#input: popularity: list[int], a list of integers
#output: int, the minimum number of swaps needed to sort the list


# Time Complexity: O(n^2)
# Space Complexity: O(1)

# def minimum_swaps(popularity: list[int]) -> int:
#     swaps = 0
#     for i in range(len(popularity)):
#         max_popularity = popularity[i]
#         for j in range(i + 1, len(popularity)):
#             if popularity[j] > max_popularity:
#                 max_popularity = popularity[j]
#         if max_popularity != popularity[i]:
#             for j in range(i + 1, len(popularity)):
#                 if popularity[j] == max_popularity:
#                     popularity[i], popularity[j] = popularity[j], popularity[i]
#                     swaps += 1

#     return swaps


# Time Complexity: O(n log n)
# Space Complexity: O(n)
def minimum_swaps(popularity: list[int]) -> int:
    # Create a list of tuples with (value, index) pairs
    indexed_popularity = list(enumerate(popularity))
    
    # Sort the list based on values in descending order
    indexed_popularity.sort(key=lambda x: x[1], reverse=True)
    
    # Create a visited array to keep track of visited elements
    visited = [False] * len(popularity)
    
    # Initialize swaps counter
    swaps = 0
    
    # Process each element
    for i in range(len(popularity)):
        # If element is visited or already in correct position
        if visited[i] or indexed_popularity[i][0] == i:
            continue
            
        # Find cycle size
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = indexed_popularity[j][0]
            cycle_size += 1
            
        # Add required swaps (cycle_size - 1)
        if cycle_size > 0:
            swaps += (cycle_size - 1)
            
    return swaps


def test_minimum_swaps():
    # Test case 1: Already sorted list (descending order)
    assert minimum_swaps([5, 4, 3, 2, 1]) == 0, "Already sorted list should require 0 swaps"
    
    # Test case 2: Reverse sorted list (ascending order)
    assert minimum_swaps([1, 2, 3, 4, 5]) == 2, "Reverse sorted list should require 2 swaps"
    
    # Test case 3: List with duplicate elements
    assert minimum_swaps([3, 3, 2, 1, 3]) == 2, "List with duplicates"
    
    # Test case 4: Small list
    assert minimum_swaps([2, 1]) == 0, "Small list"
    
    # Test case 5: List with all same elements
    assert minimum_swaps([4, 4, 4, 4]) == 0, "List with all same elements should require 0 swaps"
    
    # Test case 6: Random order list
    assert minimum_swaps([3, 4, 1, 2]) == 2, "Random order list"
    
    # Test case 7: Empty list
    assert minimum_swaps([]) == 0, "Empty list should require 0 swaps"
    
    # Test case 8: Single element list
    assert minimum_swaps([1]) == 0, "Single element list should require 0 swaps"
    
    # Test case 9: List with negative numbers
    assert minimum_swaps([-1, -5, -3, -2, -4]) == 2, "List with negative numbers"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_minimum_swaps()