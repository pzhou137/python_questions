#input: a: list[int], b: list[int], k: int
#output: int, the maximum number of distinct integers in the array a after max k swaps between a and b


#key point: use set to find the distinct integers
def getMaximumDistinctCount1(a: list[int], b: list[int], k: int) -> int:
    #create a frequency map for a and b
    freq_a = {}
    for i in range(len(a)):
        freq_a[a[i]] = freq_a.get(a[i], 0) + 1

    freq_b = {}
    for i in range(len(b)):
        freq_b[b[i]] = freq_b.get(b[i], 0) + 1
        
    #create a set of distinct integers in a
    distinct_a = set(a)
    #create a set of distinct integers in b
    distinct_b = set(b)

    #find the intersection of distinct_a and distinct_b
    # new_elements = distinct_a.difference(distinct_b)
    new_elements = [x for x in distinct_b if x not in distinct_a]
    # new_elements.sort(key=lambda x: freq_b[x], reverse=True)

    # potential_swaps = min(len(new_elements), len(a)-len(distinct_a), k)


    swaps = 0
    added_distinct = 0

    for elem in new_elements:
        if swaps < k:
            # if elem not in freq_a:
            added_distinct += 1
            swaps += 1
            if swaps == k:
                break
        else:
            break

    potential_distinct = len(distinct_a) + added_distinct

    return min(potential_distinct, len(a))
    


def getMaximumDistinctCount(a: list[int], b: list[int], k: int) -> int:
    #create a frequency map for a and b
    # freq_a = {}
    # for i in range(len(a)):
    #     freq_a[a[i]] = freq_a.get(a[i], 0) + 1

    # freq_b = {}
    # for i in range(len(b)):
    #     freq_b[b[i]] = freq_b.get(b[i], 0) + 1
        
    #create a set of distinct integers in a
    distinct_a = set(a)
    #create a set of distinct integers in b
    distinct_b = set(b)

    #find the intersection of distinct_a and distinct_b
    # new_elements = distinct_a.difference(distinct_b)
    
    new_elements = [x for x in distinct_b if x not in distinct_a]
    # this is the same as the above
    # new_element2 = []
    # for x in distinct_b:
    #     if x not in distinct_a:
    #         new_element2.append(x)

    potential_swaps = min(len(new_elements), len(a)-len(distinct_a), k)
    return potential_swaps + len(distinct_a)
    


# Test cases
def test_get_max_distinct_count():
    # Test case 1: Basic case
    a1 = [1, 1, 2, 3]
    b1 = [4, 5, 6, 6]
    k1 = 2
    assert getMaximumDistinctCount(a1, b1, k1) == 4, "Test case 1 failed"
    
    # Test case 2: No duplicates in a
    a2 = [1, 2, 3, 4]
    b2 = [5, 6, 7, 8]
    k2 = 2
    assert getMaximumDistinctCount(a2, b2, k2) == 4, "Test case 2 failed"
    
    # Test case 3: All duplicates in a
    a3 = [1, 1, 1, 1]
    b3 = [2, 3, 4, 5]
    k3 = 3
    assert getMaximumDistinctCount(a3, b3, k3) == 4, "Test case 3 failed"
    
    # Test case 4: k = 0
    a4 = [1, 1, 2, 2]
    b4 = [3, 4, 5, 6]
    k4 = 0
    assert getMaximumDistinctCount(a4, b4, k4) == 2, "Test case 4 failed"
    
    # Test case 5: k larger than necessary
    a5 = [1, 1, 1, 1]
    b5 = [2, 2, 3, 3]
    k5 = 10
    assert getMaximumDistinctCount(a5, b5, k5) == 3, "Test case 5 failed"
    
    print("All test cases passed!") 
    
# Run the tests
test_get_max_distinct_count()
        
        
        
    