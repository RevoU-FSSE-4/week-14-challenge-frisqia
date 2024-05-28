def is_anagram(s1: str, s2: str) -> bool:
    """
    This function checks if the two given strings `s1` and `s2` are anagrams.
    
    Two strings are anagrams if they contain the same characters with the same frequencies,
    ignoring spaces and capitalization.
    
    Args:
    - s1 (str): The first input string.
    - s2 (str): The second input string.
    
    Returns:
    - bool: True if the strings are anagrams, False otherwise.
    
    Examples:
    - is_anagram("Listen", "Silent") should return True
    - is_anagram("hello", "billion") should return False
    """
    def hapus_str(s):
        hapus = {}
        for i in s.lower():
            if i.isalpha():
                if i in hapus:
                    hapus[i] += 1
                else:
                    hapus[i] = 1
        return hapus

    hapus_s1 = hapus_str(s1)
    hapus_s2 = hapus_str(s2)
    
    return hapus_s1 == hapus_s2

# You can test your function with print statements below
# Example:
print(is_anagram("Listen", "Silent"))  # Expected output: True
print(is_anagram("hello", "billion"))  # Expected output: False


