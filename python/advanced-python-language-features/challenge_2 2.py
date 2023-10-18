# Challenge:
# Print a dictionary that contains:
# Length
# Digits
# Punctuation
# Uniq Letters
# Uniq Count
# from a given string
import pprint
import string

test_string = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwism $50!"

# Solution:

str_data = {
    'length': len(test_string),
    'digits': len([x for x in test_string if x.isdigit()]),
    'punctuation': len([x for x in test_string if x in string.punctuation]),
    'Unique Letters': "".join({x for x in test_string if x.isalpha()}),
    'Unique Count': len({x for x in test_string if x.isalpha()})
}

pprint.pp(str_data)

