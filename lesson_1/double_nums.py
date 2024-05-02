def is_double(num):
    str_num = str(num)
    mid_idx = len(str_num) // 2
    left_num = str_num[:mid_idx]
    right_num = str_num[mid_idx:]

    return left_num == right_num

def twice(num):
    if is_double(num):
        return num
    else:
        return num * 2
    
print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True