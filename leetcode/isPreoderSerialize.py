def isValidSerialization(preorder: str) -> bool:
    preorder = preorder.split(',')
    print(preorder)
    null_value = preorder.count('#')
    print(null_value)
    total = len(preorder)
    value = total - null_value
    print(value)
    if null_value == value:
        return False
    return True

print(isValidSerialization("1,#"))