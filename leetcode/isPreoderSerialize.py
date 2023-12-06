def isValidSerialization(preorder: str) -> bool:
    preorder = preorder.split(',')
    slot = 1
    
    for node in preorder:
        slot -= 1
        if slot < 0:
            return False
        if node != '#':
            slot += 2
    return slot == 0

print(isValidSerialization("1,#"))