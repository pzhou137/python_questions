def array_challenge(arr: list[int]) -> list[int]:
    result = [0 for _ in range(len(arr))]
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                result[i] += arr[i] - arr[j]
            elif arr[j] > arr[i]:
                result[i] -= arr[j] - arr[i]
            else:
                continue
    # print(result)
    return result


def array_challenge2(arr: list[int]) -> list[int]:
    result = [0] * len(arr)
    prefix_sum = 0
    for i in range(1, len(arr)):
        prefix_sum += arr[i - 1]
        result[i] = i * arr[i] - prefix_sum
    print("array_challenge2", result)
    return result


def test_array_challenge():
    # assert array_challenge([1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4]
    # assert array_challenge([5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0]
    # assert array_challenge([1, 3, 2, 4, 5]) == [0, 2, 1, 3, 4]
    assert array_challenge2([2, 4, 3]) == [0, 2, 0]
    print("All test cases passed!")

if __name__ == "__main__":
    test_array_challenge()




