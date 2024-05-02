def triangle(size):
    for j in range(1, size + 1):
        print(' ' * (size - j) + '*' * j)
    print()
            
triangle(5)
triangle(9)