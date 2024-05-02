def consecutive_ints():
    num = int(input("Please enter an integer greater than 0: "))
    operation = input('Enter "s" to compute the sum, '
                      'or "p" to compute the product: ')
    if operation == 's':
        return sum(num)
    elif operation == 'p':
        return product(num)

def sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"The sum of the integers between 1 and {n} is {sum}.")

def product(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    print(f"The product of the integers between 1 and {n} is {product}.")

consecutive_ints()