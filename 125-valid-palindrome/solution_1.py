def is_palindrome(input_string):
    if not input_string:
        return False

    left_idx, right_idx = 0, len(input_string) -1
    while left_idx < right_idx:
        if input_string[left_idx] != input_string[right_idx]:
            return False
        left_idx += 1
        right_idx -= 1
    return True


print(is_palindrome('a'))
print(is_palindrome('aa'))
print(is_palindrome('abba'))
print(is_palindrome('abcba'))
print(is_palindrome('abc'))
print(is_palindrome('aacbbc'))
print(is_palindrome('daabb'))