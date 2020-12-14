# This file is required. Use the same name, "source.py".
# All of your *foundational* code goes here, meaning the functions and classes
# that can be used to build larger processes. For example, the class you
# created for the OOP assignment would go here.

# Here is a test class, replace the code below with your own
import numpy as np
import panads as pd
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

    # this function calculates the value of the exponential friction factor K, this value is calculated for each pipe within each loop
    def k_formula(self):

        for i in range(self.num_loops):

            for j in range(len(self.loops[i + 1])):
                k = (4.73 * float(self.loops[i + 1][j][1])) / (
                            (float(self.loops[i + 1][j][0]) ** 4.87) * (float(self.loops[i + 1][j][2]) ** 1.85))
                self.loops[i + 1][j].append(k)
                print("For Loop", i, "For Pipe", j, "The K Value is:", k)

        # this function calculates the value of headloss in each pipe within each loop
        def hf_formula(self):
            for i in range(self.num_loops):
                for j in range(len(self.loops[i + 1])):
                    if (self.loops[i + 1][j][3]) > 0:
                        h = self.loops[i + 1][j][4] * (self.loops[i + 1][j][3] ** 1.85)
                    elif (self.loops[i + 1][j][3]) < 0:

                        h = self.loops[i + 1][j][4] * (abs(self.loops[i + 1][j][3]) ** 1.85)
                        h = h * -1

                    self.loops[i + 1][j].append(h)
                    print("For Loop", i, "For Pipe", j, "The hf Value is:", h)

            # this function calculates the ratio between headloss and the inital flowrate the user inputed

            def ratio_formula(self):
                for i in range(self.num_loops):
                    for j in range(len(self.loops[i + 1])):
                        ratio = self.loops[i + 1][j][5] / self.loops[i + 1][j][3]
                        self.loops[i + 1][j].append(ratio)
                        print("For Loop", i, "For Pipe", j, "The ratio Value is:", ratio)
                        # this function calculates the error developed from the formulas used above, then the error is added to the inital flowrate that was assumed to correct the flowarte value

                def q_corrected_formula(self):

                    hsums = []
                    rsums = []

                    for i in range(self.num_loops):
                        sums = 0
                        sums2 = 0
                        for j in range(len(self.loops[i + 1])):
                            sums += self.loops[i + 1][j][5]
                            sums2 += self.loops[i + 1][j][6]

                        hsums.append(abs(sums))
                        rsums.append(abs(sums2))

                    for i in range(self.num_loops):
                        for j in range(len(self.loops[i + 1])):
                            q_corrected = self.loops[i + 1][j][3] + (-1 * hsums[i]) / (1.85 * rsums[i])
                            self.loops[i + 1][j].append(q_corrected)
                            self.loops[i + 1][j].append((-1 * hsums[i]) / (1.85 * rsums[i]))
                            print("For Loop", i, "For Pipe", j, "The q_corrected value is:", q_corrected)
                            print("For Loop", i, "For Pipe", j, "The error value is:",
                                 (-1 * hsums[i]) / (1.85 * rsums[i]))

                            # this function calls all formulas

                def calculations(self):
                    self.k_formula()
                    self.hf_formula()
                    self.ratio_formula()
                    self.q_corrected_formula()

                # this function checks for the iternations
                def output(self):

                    self.calculations()

                    data = {"Loop": [],
                            "Pipe": [],
                            "K": [],
                            "Flow Rate": [],
                            "HeadLoss": [],
                            "Ratio": [],
                            "Flow Rate Corrected": [],
                            "Error": []
                            }

                    for i in range(self.num_loops):
                        for j in range(len(self.loops[i + 1])):
                            data["Loop"].append(i)
                            data["K"].append(self.loops[i + 1][j][4])
                            data["Flow Rate"].append(self.loops[i + 1][j][3])
                            data["HeadLoss"].append(self.loops[i + 1][j][5])
                            data["Ratio"].append(self.loops[i + 1][j][6])
                            data["Flow Rate Corrected"].append(self.loops[i + 1][j][7])
                            data["Error"].append(self.loops[i + 1][j][8])

                    lst = []
                    for i in range(self.num_loops):
                        for j in range(len(self.loops[i + 1])):
                            if (data["Error"][i] > 0.009):
                                lst.append(i)
                            if i in lst:
                                data["Error"][i] = self.loops[i + 1][j][8]
                                self.loops[i + 1][j][3] = self.loops[i + 1][j][7]
                    self.output()


# we do another interation if formula is greater than 0.009

# loops = [[["AB", [L,D,C], K, Q, , H, ratio, Q_Corrected]]]

# each index is a list that represents a loop, each index within that
# list is a pipe, each index represents key values
'''
loops = {
    1:[
        [L,D,C,Q (Flow Rate),K (Exponential Friction Factor),HF(headloss) ,ratio,Q_Corrected], 

        [L,D,C,Q,K,HF,ratio,Q_Corrected]],

    2:[[,L,D,C,Q,K,HF,ratio,Q_Corrected],[,L,D,C,Q,K,HF,ratio,Q_Corrected]]

    }

'''

'''
        status = true
        while status == true:
            #Code to display table
            if data["Error"][-1]<=0.009:
                break

            for i in range (self.num_loops): 
                for j in range (len(self.loops[i+1])):

                    self.loops[i+1][j][3] = self.loops[i+1][j][7]

            self.calculations()
            for i in range (self.num_loops): 
                for j in range (len(self.loops[i+1])):
                    data["Error"][i]= self.loops[i+1][j][8]
              '''
