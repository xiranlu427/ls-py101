def crunch(string):
    if string == "":
        return ""
    result = string[0]
    for char in range(1, len(string)):
        if char == result[-1]:
            continue
        else:
            result += char
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')