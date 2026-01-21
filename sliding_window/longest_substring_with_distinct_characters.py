def longestDistinctSubstringLen(s: str) -> int:
    # TODO: Implement on your own
    # Return length of the longest substring with all distinct characters
    pass


def main():
    tests = [
        # Given examples
        ("geeksforgeeks", 7),      # "eksforg"
        ("aaa", 1),                # "a"
        ("abcdefabcbb", 6),        # "abcdef"

        # Edge cases
        ("", 0),                   # empty string
        ("a", 1),                  # single char
        ("ab", 2),                 # all distinct short

        # All distinct
        ("abcdefghijklmnopqrstuvwxyz", 26),

        # All same
        ("bbbbbbbb", 1),

        # Repeats that force frequent window shifts
        ("abba", 2),               # "ab" or "ba"
        ("pwwkew", 3),             # "wke" (classic)
        ("dvdf", 3),               # "vdf"
        ("anviaj", 5),             # "nviaj"

        # Repeated pattern
        ("abcabcabc", 3),          # "abc"

        # Numbers/symbols (should work the same)
        ("a1b2c3a1", 6),            # "a1b2c3"
        ("!@#!!@#", 3),             # "!@#"

        # Mixed repeats
        ("tmmzuxt", 5),             # "mzuxt"
        ("bbtablud", 6),            # "tablud"
    ]

    for s, expected in tests:
        got = longestDistinctSubstringLen(s)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status} | s={s!r} | expected={expected} | got={got}")


if __name__ == "__main__":
    main()
