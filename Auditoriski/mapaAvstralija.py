from constraint import *


def diffColours(col1, col2):
    return col1 != col2


if __name__ == '__main__':
    problem = Problem()
    variables = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
    colours = ["red", "blue", "green"]
    problem.addVariables(variables, colours)
    pairs = [("WA", "NT"), ("WA", "SA"), ("NT", "SA"), ("NT", "Q"), ("SA", "Q"), ("SA", "NSW"), ("Q", "NSW"),
             ("NSW", "V"), ("SA", "V")]
    for p in pairs:
        problem.addConstraint(diffColours, p)
    print(problem.getSolution())
    print(problem.getSolutions())
    res_iter = problem.getSolutionIter()
    for i in range(5):
        print(next(res_iter))
