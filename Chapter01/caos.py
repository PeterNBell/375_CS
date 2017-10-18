
def main():
    print("This program simulates the caos")
    x = eval(input("Enter a number between 0 and 1"))
    y = eval(input("How many times should we loop this?"))
    for i in range(0, y):

        x = 3.9 * x * (1 - x)
        print(x)
main()

