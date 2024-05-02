def center_of(string):
    mid_idx = (len(string) - 1) // 2
    if len(string) % 2 == 1:
        return string[mid_idx]
    else:
        return string[mid_idx:mid_idx + 2]
    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True