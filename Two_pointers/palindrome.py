def is_palindrome(text: str) -> bool:
    left, right = 0, len(text)-1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].lower() != text[right].lower():
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    print(is_palindrome("ra cec,, a r"))