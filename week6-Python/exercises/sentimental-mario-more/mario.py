from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

for i in range(n):
    for k in range(n - 1, i, -1):
        print(" ", end="")
    for j in range(i + 1):
        print("#", end="")
    for x in range(1):
        print("  ", end="")
    for z in range(i + 1):
        print("#", end="")

    print()
