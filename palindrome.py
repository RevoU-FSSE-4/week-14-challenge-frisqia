# palindrome.py

def is_palindrome(s: str) -> bool:
    """
    This function checks if the given string `s` is a palindrome.
    
    A palindrome is a word, phrase, number, or other sequence of characters 
    that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    
    Args:
    - s (str): The input string.
    
    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    
    Examples:
    - is_palindrome("A man, a plan, a canal, Panama") should return True
    - is_palindrome("racecar") should return True
    - is_palindrome("hello") should return False
    """
    cleaned_str = []
    for i in s:
        if i.isalpha():
            cleaned_str.append(i.lower())
    count = 0
    for i in cleaned_str:
        count += 1
    left, right = 0, count - 1
    while left < right:
        if cleaned_str[left] != cleaned_str[right]:
            return False
        left += 1
        right -= 1
    return True
    
# You can test your function with print statements below
# Example:
print(is_palindrome("A man, a plan, a canal, Panama"))  # Expected output: True
print(is_palindrome("racecar"))  # Expected output: True
print(is_palindrome("hello"))  # Expected output: False
