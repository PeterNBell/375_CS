def main():
    x = eval(input("Input a meters per second value, and don't you dare put no commas")) #This makes sure that there will be no commas inputed as anx value
    if x < 0: #if X is a negative number print Invalid Input
        print("Invalid input")
    y = x * 2.23694
    if x == 1: #Getting the right sintax for mile per hour
        print(x, "meter per second =", y, "miles per hour")
    else: #To prevent 1 from printing twice
        if x >= 0: #Same calculation for 1 not equal to 0 and is positive
            print(x, "meters per second =", y, "miles per hour")
main()
