# scenario that we may have any charaters including spaces
def is_palindrome(input_string):
    left_idx = 0
    right_idx = len(input_string) - 1
    while left_idx < right_idx:
        if not input_string[left_idx].isalnum():
            left_idx += 1
            continue # go back tp the befiining of the while loop, ignore remaining lines
        if not input_string[right_idx].isalnum():
            right_idx -= 1
            continue # go back to the beginning of the while loop, ignore remaining lines
        if input_string[left_idx].lower() != input_string[right_idx].lower():
            return False
        return True

print(is_palindrome('a'))
print(is_palindrome('aa'))
print(is_palindrome('abba'))
print(is_palindrome('abcba')) # len 5, mid = 2
print(is_palindrome('abc'))   # len 3, mid = 1
print(is_palindrome('aacbbc'))
print(is_palindrome('daabb')) # len 5, mid = 2
print(is_palindrome('A man, a plan, a canal: Panama'))