def solution(brackets):

    stack = []
    for b in brackets:
        if b == "(":
            stack.append(b)
        elif b == ")":
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True