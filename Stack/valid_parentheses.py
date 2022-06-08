def isValid_parentheses(s):
    stack=[]
    # define a hashmap to valid parentheses
    closeToopen={
        ")":"(",
        "]":"[",
        "}":"{"
    }
    for c in s :
        if c in closeToopen:
            if stack and stack[-1]==closeToopen[c]:
                stack.pop()
            else:
                return False
        else:
         stack.append(c)
    return True if not stack else False


print(isValid_parentheses("[[[[[(((())))]]]]]"))
print(isValid_parentheses("{{{()}}}"))
print(isValid_parentheses("{}{}()()[]"))