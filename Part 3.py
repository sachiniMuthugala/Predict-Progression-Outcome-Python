#Part 3

import time

done = True  # this is a boolean flag variable.done only can have True/False
# This programme will repeat as long as done = True

numberOfProgressStudents = 0
numberOfExcludeStudents = 0
numberOfTrailingStudents = 0
numberOfRetrieverStudents = 0

while done:  # while loop repeats as long as condition is True
    time.sleep(0.3)
    print()
    response = input("Press any key to input credits OR press 'q' to quit:")
    response = response.lower()

    if (response != "q"):  # it will run if user does NOT input "q".else it will show final results

        def Validity(credits):  # user define function
            if (credits % 20 != 0 or credits > 120 or credits < 0):
                print("Range error")
                return True  # it will be true if there is an error
            else:
                return False


        while True:

            try:
                isValid = True  # isValid is a variable which checks there is an error or not
                while (isValid):  # this will run till the isValid = False

                    pass_credits = int(input("Please enter number of pass credits  : "))
                    isValid = Validity(pass_credits)

                isValid = True
                while (isValid):
                    defer_credits = int(input("Please enter number of defer credits : "))
                    isValid = Validity(defer_credits)

                isValid = True
                while (isValid):
                    fail_credits = int(input("Please enter number of fail credits  : "))
                    isValid = Validity(fail_credits)

                total_credits = pass_credits + defer_credits + fail_credits

                if (total_credits == 120):

                    if (pass_credits == 120):
                        numberOfProgressStudents += 1
                    elif (pass_credits == 100):
                        numberOfTrailingStudents += 1
                    elif (fail_credits >= 80):
                        numberOfExcludeStudents += 1
                    else:
                        numberOfRetrieverStudents += 1

                    time.sleep(0.3)
                    print("Next Student....")

                    break
                else:
                    print("Total incorrect.Try Again!")


            except ValueError:
                print("Integers required.Try Again!")



    else:
        done = False  # done will be False when user enter "q"

        print("-" * 6, " Horizontal Histogram ", "-" * 6)
        print()
        print("{:^12s}".format("Progress") + "{:^12s}".format("Trailing") + "{:^12s}".format("Retriever") + "{:^12s}".format("Excluded"))


        if numberOfProgressStudents >= numberOfTrailingStudents and numberOfProgressStudents>= numberOfExcludeStudents and numberOfProgressStudents>= numberOfRetrieverStudents:
            highest = numberOfProgressStudents
        elif numberOfTrailingStudents >= numberOfExcludeStudents and numberOfTrailingStudents>= numberOfRetrieverStudents:
            highest = numberOfTrailingStudents
        elif numberOfExcludeStudents>=numberOfRetrieverStudents:
            highest = numberOfExcludeStudents
        else:
            highest = numberOfRetrieverStudents


        for i in range(highest):
            line = ""  # line = Empty string

            if i < numberOfProgressStudents:  # because range starts with 0
                symbol = "*"
            else:
                symbol = " "

            line += "{:^12s}".format(symbol)  # "^" this will align the stars in the middle
            # it will print stars in the middle of 12 columns.(6th column)


            if i < numberOfTrailingStudents:
                symbol = "*"
            else:
                symbol = " "

            line += "{:^12s}".format(symbol)

            if i < numberOfRetrieverStudents:
                symbol = "*"
            else:
                symbol = " "

            line += "{:^12s}".format(symbol)

            if i < numberOfExcludeStudents:
                symbol = "*"
            else:
                symbol = " "

            line += "{:^12s}".format(symbol)

            print(line)

        print()
        print((numberOfExcludeStudents + numberOfTrailingStudents + numberOfRetrieverStudents + numberOfProgressStudents)," outcomes in total")



