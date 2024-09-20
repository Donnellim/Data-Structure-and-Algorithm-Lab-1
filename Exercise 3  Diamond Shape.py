number = int(input("Enter a number: "))
n = number

def print_diamond(n):
    if n % 2 == 0:
        return print("Please provide an odd integer.")
    
    mid_row = n // 2

    for i in range(mid_row + 1):
        num_spaces = mid_row - i
        num_stars = 2 * i + 1
        print(' ' * num_spaces + '*' * num_stars)

    for i in range(mid_row - 1, -1, -1):
        num_spaces = mid_row - i
        num_stars = 2 * i + 1
        print(' ' * num_spaces + '*' * num_stars)

print_diamond(n)