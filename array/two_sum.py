

from typing import List


def two_sum_exists_hashset(arr: List[int], target: int) -> bool:
    seen = set()
    for x in arr:
        if (target - x) in seen:
            return True
        seen.add(x)
    return False

def run_tests(fn):
    tests = [
        # (arr, target, expected)
        ([0, -1, 2, -3, 1], -2, True),    # -3 + 1
        ([1, 2, 3, 4], 8, False),
        ([3, 3], 6, True),               # duplicate value, distinct indices
        ([3], 6, False),
        ([], 0, False),
        ([5, -2, -1, 10], 8, True),       # -2 + 10
        ([2, 7, 11, 15], 9, True),        # 2 + 7
        ([2, 7, 11, 15], 10, False),
        ([0, 0, 0], 0, True),             # 0 + 0
        ([-5, -4, -3, -2], -7, True),     # -5 + -2
    ]

    for i, (arr, target, expected) in enumerate(tests, start=1):
        got = fn(arr, target)
        if got != expected:
            raise AssertionError(
                f"Test {i} failed for {fn.__name__}: arr={arr}, target={target}, "
                f"expected={expected}, got={got}"
            )
    print(f"All tests passed for {fn.__name__}")


def main():

    run_tests(two_sum_exists_hashset)



if __name__ == "__main__":
    main()
