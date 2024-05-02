def stringy(num):
    result = ""
    for idx in range(num):
        digit = '1' if idx % 2 == 0 else '0'
        result += digit
    return result