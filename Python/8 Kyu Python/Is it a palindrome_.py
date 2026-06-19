def is_palindrome(s) -> bool:
    return True if s.lower() == s.lower()[::-1] else False