#Part 1

def Validity(credits):      #user define function to check range.
    if (credits % 20 != 0 or credits > 120 or credits < 0):
        print("Range error.Try Again!")
        return True  #it holdings a value true
    else:
        return False


while True:

        try:
            isValid = True      #isValid is a variable which checks there is an error or not.
            while(isValid):     #this will run till the isValid = False.

                pass_credits = int(input("please enter number of pass credits  : "))
                isValid = Validity(pass_credits)    #isValid holding a value coming from "return".

            isValid = True
            while (isValid):

                defer_credits = int(input("please enter number of defer credits : "))
                isValid = Validity(defer_credits)

            isValid = True
            while (isValid):

                fail_credits = int(input("please enter number of fail credits  : "))
                isValid = Validity(fail_credits)

            total_credits = pass_credits + defer_credits + fail_credits


            if (total_credits == 120):

                if (pass_credits == 120):
                    development = "Progress"
                elif (pass_credits == 100):
                    development = "Progress - module trailer"
                elif (fail_credits >= 80):
                    development = "Exclude"
                else:
                    development = "Do not Progress - module retriever"
                print("Progress outcome: " , development)
                break


            else:
                print("Total incorrect.Try Again!")

        except ValueError:
            print("Integers required.Try Again!")
            
            
           



















