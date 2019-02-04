from __future__ import print_function
import math
import logging


def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'


def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n."""
    result = []
    a = 1
    b = 1
    while a < n:
        result.append(a)
        tmp_var = b
        b = a + b
        a = tmp_var
    return result

# holds the different cognitive architectures that we have available
class Architectures:
    def __init__(self, cogArchConfig):
        self.cogArchConfig = cogArchConfig #holds the configuration file



# the environments we can test our agents in
class Environments:
    def __init__(self, envConfig):
        self.envConfig = envConfig #holds the configuration file



class Utilities:

    def readFile(file):

        f = open(file, "r")   # here we open file "input.txt". Second argument used to identify that we want to read file
                                     # Note: if you want to write to the file use "w" as second argument

        for line in f.readlines():   # read lines
            print(line)

        f.close()                   # It's important to close the file to free up any system resources.

    def writeFile(fileName):

        logging.info('Calling write file')

        if len(fileName) is 0:
            logging.warning("file is null")

        f = open(file, "a")

        for i in range(5):
            f.write(i)

        f.close()




if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(fib(10))




