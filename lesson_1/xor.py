def xor(arg1, arg2):
    if arg1: 
        return False if arg2 else True
    elif arg2:
        return True
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)