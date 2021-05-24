def is_palindrome(input_string):
    if not input_string:
        return False
    len_string = len(input_string)
    if len_string % 2 == 0:
        # even scenario abba
        left_idx  = len_string // 2 - 1
        right_idx = len_string // 2
    else:
        # odd scenario abcba
        left_idx = right_idx = len_string // 2

    while left_idx >= 0 and right_idx < len_string:
        if input_string[left_idx] != input_string[right_idx]:
            return False
        left_idx -= 1
        right_idx += 1
    return True

print(is_palindrome('a'))
print(is_palindrome('aa'))
print(is_palindrome('abba'))
print(is_palindrome('abcba')) # len 5, mid = 2
print(is_palindrome('abc'))   # len 3, mid = 1
print(is_palindrome('aacbbc'))
print(is_palindrome('daabb')) # len 5, mid = 2