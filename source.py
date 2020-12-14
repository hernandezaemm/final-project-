# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# Here is a test class, replace the code below with your own
class Calculator:
    def __init__(self, loops):
        self.num_loops = loops
        self.loops = {}

        # this function asks for the user to input the information for the pipe network, first they have to specify how many loops there are in the network, then for each pipe in each loop the user inputsthe diameter, length, Hazen friction factor, and the inital flowrate guess
        def user_input(self):
            value = 0

            for i in range(self.num_loops):
                print("\nPlease enter number of pipes for loop", i + 1)
                num_pipes = int(input())
                self.loops[i + 1] = []
                for j in range(num_pipes):
                    self.loops[i + 1].append([])
                    print(
                        "\nEnter diameter, length, Hazen friction factor, and flow rate for pipe separated by commas for pipe",
                        j + 1)
                    inputs = input()
                    inputs = inputs.split(",")
                    for k in range(len(inputs)):
                        value = float(inputs[k])
                        self.loops[i + 1][j].append(value)
