def binary_search(arr: list[int], target: int) -> int:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid: int = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    arr: list[int] = [
        1,
        3,
        7,
        9,
        10,
        14,
        18,
        23,
        27,
        30,
        38,
        43,
        48,
        55,
        56,
        62,
        75,
        82,
        91,
        99,
    ]

    print(binary_search(arr, 18))

