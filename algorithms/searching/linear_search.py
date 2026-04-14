def linear_search(arr: list[int], target: int) -> list[int]:
    res: list[int] = [idx for idx, num in enumerate(arr) if num == target]

    return res


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

    print(linear_search(arr, 18))

