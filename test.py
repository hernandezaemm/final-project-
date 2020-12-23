# This file is required. Use the same name, "test.py". Below you see an example
# of importing a class from "source.py", instantiating a new object and printing
# that object. Replace the code below with your own.

from source import Calculator


# number in calculator is how many loops there are in the system of pipes
def main():
    test = Calculator(1)
    test.user_input()
    while test.output():
        test.output()


if __name__ == "__main__":
main()
