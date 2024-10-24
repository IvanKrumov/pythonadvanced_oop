n = int(input())


def print_upper_part(n):
    for row in range(1, n +1):
        print(" "*(n-row) + "* " * row)


def print_bottom_part(n):
    for row in range(n-1, 0, -1):
        print(" "*(n-row) + "* " * row)

print_upper_part(n)
print_bottom_part(n)