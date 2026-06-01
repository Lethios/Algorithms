def counting_sort(arr: list[int]) -> list[int]:
    arr: list[int] = arr.copy()
    max_element: int = max(arr)

    freq_arr: list[int] = [0] * (max_element + 1)
    for num in arr:
        freq_arr[num] += 1

    arr: list[int] = []
    for num in range(len(freq_arr)):
        while freq_arr[num] > 0:
            arr.append(num)
            freq_arr[num] -= 1

    return arr


if __name__ == "__main__":
    arr: list[int] = [
        38,
        27,
        43,
        3,
        9,
        82,
        10,
        1,
        75,
        56,
        14,
        62,
        48,
        91,
        23,
        7,
        55,
        30,
        18,
        99,
    ]

    print(counting_sort(arr))
