from typing import List

def max_sum_subarray_k(arr: List[int], k: int) -> int:
    # Assumes: 1 <= k <= len(arr)
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]        # add incoming
        window_sum -= arr[i - k]    # remove outgoing
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


def main() -> None:
    test_cases = [
        ([100, 200, 300, 400], 2, 700),
        ([1, 4, 2, 10, 23, 3, 1, 0, 20], 4, 39),
        ([100, 200, 300, 400], 1, 400),
        ([5], 1, 5),
        ([-1, -2, -3, -4], 2, -3),
    ]

    for i, (arr, k, expected) in enumerate(test_cases, start=1):
        result = max_sum_subarray_k(arr, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"{i:02d}. {status} | arr={arr}, k={k} | expected={expected}, got={result}")


if __name__ == "__main__":
    main()
