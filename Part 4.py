#Part 4

#List inside the List = nested List
#2 dimentional lists
studentList = [[120, 0, 0], [100, 20, 0], [100, 0, 20], [80, 20, 20], [60, 40, 20], [40, 40, 40], [20, 40, 60], [20, 20, 80], [20, 0, 100], [0, 0, 120]]

numberOfProgressStudents = 0
numberOfExcludeStudents = 0
numberOfTrailingStudents = 0
numberOfRetrieverStudents = 0

for individual in studentList:
    try:
        pass_credits = int(individual[0])
        defer_credits = int(individual[1])
        fail_credits = int(individual[2])

        total_credits = pass_credits + defer_credits + fail_credits


        if (pass_credits % 20 == 0 and defer_credits % 20 == 0 and fail_credits % 20 == 0):
            if (total_credits == 120):

                if (pass_credits == 120):
                    numberOfProgressStudents += 1
                elif (pass_credits == 100):
                    numberOfTrailingStudents += 1
                elif (fail_credits >= 80):
                    numberOfExcludeStudents += 1
                else:
                    numberOfRetrieverStudents += 1


            else:
                print("Total incorrect")
        else:
            print("Range error")
    except ValueError:
        print("Integers required")



print("-"*3 , "Progression Outcome" , "-"*3)
print()

def students(count,name):
    stars = ""

    for i in range(count):
        stars += "*"
    print(f'{name:9}  {count:>2} {":":2}' , stars) #f'{}' defines how many spaces
                                                    #">" count in right justify.without it will justify left
students(numberOfProgressStudents,"progress")
students(numberOfTrailingStudents,"Trailing")
students(numberOfRetrieverStudents,"Retriever")
students(numberOfExcludeStudents,"Exclude")



print()
print((numberOfExcludeStudents + numberOfTrailingStudents + numberOfRetrieverStudents + numberOfProgressStudents)," outcomes in total")

print("Progress:" , numberOfProgressStudents , ", Trailing:" , numberOfTrailingStudents , ", Retriever:" , numberOfRetrieverStudents , ", Exclude:" , numberOfExcludeStudents)
