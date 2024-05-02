def short_long_short(str_1, str_2):
    if len(str_1) < len(str_2):
        short = str_1
        long = str_2
    else:
        short = str_2
        long = str_1

    return short + long + short
    
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")