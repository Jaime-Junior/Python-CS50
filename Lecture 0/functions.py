def main():
    x = float(input("What's X?"))
    print("X squared is", square(x))

def square(n):
    return pow(n, 2)

main()