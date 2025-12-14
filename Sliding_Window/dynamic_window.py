from collections import defaultdict
def dynamic_window(text: str) -> int:
    longest = 0
    left = 0
    counter: dict[str, int] = defaultdict(int)
    for right in range(len(text)):
        counter[text[right]] += 1
        while counter[text[right]] > 1:
            counter[text[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
    return longest

if __name__ == "__main__":
    print(dynamic_window("aabcccedbaccaaa"))