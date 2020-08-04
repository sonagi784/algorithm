while True:
    string = input()
    if string == '.': break;

    stack = []
    flag = True
    for c in string:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ']':
            if not stack or (stack.pop() != '['):
                flag = False
        elif c == ')':
            if not stack or (stack.pop() != '('):
                flag = False

    print('yes' if flag and not stack else 'no')
