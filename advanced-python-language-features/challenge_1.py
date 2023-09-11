# Challenge:
# Write a function that perfoems the following actions:
# 1. accepts a variable number of strings and numbers. Other type ignored
# 2. accepts a keyword-only argument to return a unique-only result
# 3. combines all the arguments into a single string
# 4. returns a string containong all arguments combined as one string
# 5. Has a docstring that describes how it works and what it does
# If the unique-only argument is True (default is False), then the result
# combined string will not contain any duplicate characters


# Solution:
def string_combiner(*args, unique_only=False):
    """Combines all the arguments into a single string.
    If the unique_only argument is True (default is False), then the result
    combined string will not contain any duplicate characters.
    """
    result = ""
    for arg in args:
        if isinstance(arg, (str, int, float)):
            result += str(arg)
    if unique_only:
        result = "".join(set(result))
    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique_only=False)
print(output)


# Solution 2 (with lambda):
def string_combiner(*args, unique_only=False):
    """Combines all the arguments into a single string.
    If the unique_only argument is True (default is False), then the result
    combined string will not contain any duplicate characters.
    """
    result = map(lambda x: str(x) if isinstance(x, (str, int, float)) else None, args)
    print(f'result map: {result}')
    result = list(result)
    print(f'result list: {result}')

    result = filter(lambda x: x is not None, result)
    print(f'result filter: {result}')

    result = "".join(result)
    print(f'result join: {result}')

    # result = "".join(list(map(lambda x: str(x) if isinstance(x, (str, int, float)) else None, args)))

    if unique_only:
        result = "".join(set(result))
    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique_only=False)
print(output)

# Solution 3 (with list comprehension):
def string_combiner(*args, unique_only=False):
    """Combines all the arguments into a single string.
    If the unique_only argument is True (default is False), then the result
    combined string will not contain any duplicate characters.
    """
    result = "".join([str(arg) for arg in args if isinstance(arg, (str, int, float))])
    if unique_only:
        result = "".join(set(result))
    return result


# test code:
print(string_combiner.__doc__)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", 1, "test", "string!", unique_only=True)
print(output)
output = string_combiner("This", "is", 1, True, "string!", unique_only=False)
print(output)
output = string_combiner("This", "is", [1, 2], "string!", unique_only=False)
print(output)
