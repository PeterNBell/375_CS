def main():
    print("Welcome to Mad Libs!!! I am about to ask you for a series of names, nouns adjectives and verbs")
    print("and then I will put them in my story")
    c = "x"
    while c != "":
        name1 = ""
        name2 = ""
        name3 = ""
        while name1 == "":
            name1 = input("Name a character")
            if name1 != "":
                break
            else:
                print("Don't do this right now")
        while name2 == "":
            name2 = input("Name another character")
            if name2 != "":
                break
            else:
                print("Don't do this right now")
        while name3 == "" :
            name3 = input("Name a final character")
            if name3 != "":
                break
            else :
                print("Don't do this right now")
        print("Your characters are named", name1, name2, "and ", name3)
        c = input("{press enter to continue or any other key to re-enter}")

main()
