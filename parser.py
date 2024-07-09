def parse(tokens):
    result = {}
    stack = [result]
    for key, value, indent in tokens:
        while len(stack) > indent // 2 + 1:
            stack.pop()
        current_dict = stack[-1]
        if value:
            current_dict[key] = value
            stack.append(current_dict[key] if isinstance(current_dict[key], dict) else {})
        else:
            current_dict[key] = {}
            stack.append(current_dict[key])
    return result