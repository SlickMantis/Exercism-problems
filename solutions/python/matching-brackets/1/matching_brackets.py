def is_paired(input_string):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}  # mapping of closing → opening

    for char in input_string:
        if char in "({[":  # opening brackets
            stack.append(char)
        elif char in ")}]":  # closing brackets
            if not stack or stack[-1] != pairs[char]:
                return False  # mismatch or empty stack
            stack.pop()  # matched, remove from stack

    return not stack  # if stack empty, all matched
