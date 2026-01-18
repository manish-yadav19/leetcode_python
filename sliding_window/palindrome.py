def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

if __name__ == "__main__":
    tests = ["racecar", "abba", "ab", "a", ""]
    for t in tests:
        print(t, is_palindrome(t))
