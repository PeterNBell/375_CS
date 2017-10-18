def main():
    print("I will tell you if this is a prime number")
    x = eval(input("type the number now"))
    z = 1
    for j in range(10):
        y = 2
        for i in range(10000):
            #print(y) this shows if y is changing
            if x / y == 2 or x / y == 3 or x / y == 4 or x / y == 5 or x / y == 6 or x / y == 7 or x / y == 8 or x / y == 9 or x / y == 10:
                print("this number is not prime")
                z = 2
                break
            y = y + 1
        if z == 2:
            break
    if z != 2:
        print("this number is prime")




main ()
