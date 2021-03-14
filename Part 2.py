#Part 2

import time

done = True  # this is a boolean flag variable.done only can have True/False.
# This programme will repeat as long as done = True.

numberOfProgressStudents = 0
numberOfExcludeStudents = 0
numberOfTrailingStudents = 0
numberOfRetrieverStudents = 0

while done:  # while loop repeats as long as condition is True.

    time.sleep(0.3)
    print()
    response = input("Press any key to input credits OR press 'q' to quit:")
    response = response.lower()

    if (response != "q"):  # it will run if user does NOT input "q".else it will show final results and stop.

        # code
        def Validity(credits):  # user define function.
            if (credits % 20 != 0 or credits > 120 or credits < 0):
                print("range error")
                return True  # it holdes a value True.
            else:
                return False


        while True:

            try:
                isValid = True  # isValid is a variable which checks there is an error or not.
                while (isValid):  # this will run till the isValid = False.

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
                    print("next student...")
                    break
                else:
                    print("Total incorrect.Try Again!")


            except ValueError:
                print("Integers required.Try Again!")


    else:
        done = False  # done will be False when user enter "q".

        print()
        print("-" * 4, "Summary Of Progression Outcome", "-" * 4)
        print()

        #printing stars

        def students(count, name):     #count and name = parameters
            stars = ""

            for i in range(count):
                stars += "*"
            print(f'{name:9}  {count:>2} {":":2}', stars)  # f'{}' defines how many spaces
                                                            # ">" count in right justify.without it will justify left
        students(numberOfProgressStudents, "progress")
        students(numberOfTrailingStudents, "Trailing")
        students(numberOfRetrieverStudents, "Retriever")
        students(numberOfExcludeStudents, "Exclude")
        
        

        print()
        print((numberOfExcludeStudents + numberOfTrailingStudents + numberOfRetrieverStudents + numberOfProgressStudents)," outcomes in total")

