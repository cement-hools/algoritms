def bracket_sequence(string):
    stack = []
    open_bracket = '([{'
    close_bracket = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for bracket in string:
        if bracket in open_bracket:
            stack.append(bracket)
        else:
            if stack:
                stack_bracket = stack.pop()
                if bracket == close_bracket[stack_bracket]:
                    continue
                return False

    return not bool(stack)


s = '{[(()]}'

print(bracket_sequence(s))
