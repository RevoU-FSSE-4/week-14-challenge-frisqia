# find_max.py

def find_max(numbers: list) -> int:
    """
    This function takes a list of numbers and returns the largest number in the list.

    Args:
    - numbers (list): A list of numbers.

    Returns:
    - int: The largest number in the list.

    Examples:
    - find_max([1, 2, 3, 4, 5]) should return 5
    - find_max([-1, -2, -3, -4, -5]) should return -1
    """
    # Implement your solution here
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    
# You can test your function with print statements below
# Example:
print(find_max([1, 2, 3, 4, 5]))  # Expected output: 5
print(find_max([-1, -2, -3, -4, -5]))  # Expected output: -1
