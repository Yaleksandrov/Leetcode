# 125 Is palindrome

## Determine if given string is a palindrome

* [ ] Option one - traverse from both sides of the string towars

  ```python
  left_index = 0
  right_index = len(input_string) - 1
  while left_index < right_index:
      # do staff
      left_index -= 1
      right_index += 1
  ```
* [ ] Option two - traverse from the middle of the string towars ends
  In this scenario we might have

  even lenght palindrome `abba`,- so mid of the string is between characters `mid = len(input_string) // 2`
  odd  lenght palindrome `abcba`,- so mid of the string is between characters `b abnd b`. So we will need to pointers `left_idx = len(input_string) // 2 - 1` and `right_idx = len(input_string) // 2`

  ```python
  input_string_len = len(input_string)
  if input_string_len % 2 == 0
      # even_scenario
      left_idx = right_idx = mid = input_string_len // 2
  else:
     # odd scenario
     left_idx = input_string_len // 2 - 1
     right_idx = input_string_len // 2

  # Move from a center towards left and right end
  while left_idx >= 0 and right_idx < input_string_len:
      # do stuff
  ```
