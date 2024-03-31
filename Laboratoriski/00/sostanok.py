from constraint import *


def available(M, S, P, v):
    if S == 0:
        return False
    if M == 0 and P == 0:
        return False
    if v not in [13, 14, 16, 19]:
        return False
    if M == 1 and v not in [14, 15, 18]:
        return False
    if P == 1 and v not in [12, 13, 16, 17, 18, 19]:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 20))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------
    problem.addConstraint(available)
    [print(solution) for solution in problem.getSolutions()]
