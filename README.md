# CE-UY 3013 Project

This file presents a description of the final project. Below is a summary of what a typical problem looks like

**This program finds the discharge of each pipe of a given closed shape, using the Hardy Cross Method. The method basically 1) assumes an initial value of flowrate in each pipe 2) calculates the exponential friction factor 3)calculates head loss of each pipe using the assumed flowrate 4) finds the ratio between head loss and the initial flowrate 5) finds the error of the initial flowrate 6) adds the error to the initial flowrate resulting in the final flowrate 7) if the error is greater than the absolute value of 0.009 then all the steps are repeated until the error reaches the value of 0.009, when recalculating the new initial flowrate was the final flowrate from the previous iteration**

**this program is designed to follow the Hazen Williams method, using the constant of 1.85 in various formulas**

*the example followed for this example uses the units of feet and seconds*

The first step to using the code, is that the user will be prompted to enter the number of pipes for loop 1 and then the diameter, length, Hazen friction factor, and initial flowrate for each pipe within the first loop. These values are to be inputted by separation of commas as shown below.

*Please enter number of pipes for loop 1*

*Enter diameter, length, Hazen friction factor, and flow rate for pipe separated by commas for pipe 1*

*0.333,100,120,1*

The code will then calculate the value of exponential friction factor (k), which is done by the equation shown below.
(https://github.com/hernandezaemm/final-project-/blob/main/k%20equation.PNG)

The code will then calculate the value of head loss (hf), which is done by the equation shown below.
(https://github.com/hernandezaemm/final-project-/blob/main/headloss.PNG)

The code will then calculate the ratio between hf and the initial flowrate

The code will then find the error from the initial flowrate and will add the error to the initial flowrate to produce the final flowrate. In order to determine if this flowrate is accurate, the value of the error is deemed to be less than the absolute value of 0.009. The equation of the error is shown below. 
(https://github.com/hernandezaemm/final-project-/blob/main/error.PNG)


The example the code was modeled after is shown below.
(https://github.com/hernandezaemm/final-project-/blob/main/diagram%201.PNG)
(https://github.com/hernandezaemm/final-project-/blob/main/pg1.PNG)
(https://github.com/hernandezaemm/final-project-/blob/main/Inkedtable_LI.jpg)