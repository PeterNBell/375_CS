def main():
    print("This is a Test average calculator")
    scores = 0 #This will be used to record how many scores have been submitted
    new_average = 0
    inputed_average = 0
    while inputed_average != "" : #Do the following until the user presses enter
        inputed_average = input("Enter a test score (press enter to quit)")# doesn't eval input until it is certain it is python code
        if inputed_average != "": #this makes sure that the code doesn't have to eval anything that isn't python code
            try:
                inputed_average = eval(inputed_average) #now it evals the code and stores it in current average
                if inputed_average >100 or inputed_average <0:
                    print(inputed_average, " is an impossible grade, re-enter the test score")
                else:
                    scores = scores + 1
                    new_average = (inputed_average + (new_average * (scores - 1))) / (scores) #this is a formula that gives more weight to the last calculated average (based on the number of scores used to calculate that average) and adds that to the latest score that the user inputs into the program
                    print("your current average is ",new_average) #allows user to see the the current average
            except SyntaxError:
                print("Ya darn typed in yer number wrong")


    print("your total average is ", new_average) #this restates the final average
main()
