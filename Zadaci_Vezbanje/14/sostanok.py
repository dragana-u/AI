from constraint import *


def attendance(m, s, p, v):
    if m == 0 and p == 0:
        return False
    if m == 1 and v not in [14, 15, 18]:
        return False
    if p == 1 and v not in [12, 13, 16, 17, 18, 19]:
        return False
    if v not in [13, 14, 16, 19]:
        return False
    return True


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", [12, 13, 14, 15, 16, 17, 18, 19])
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------

    # ----------------------------------------------------
    problem.addConstraint(attendance, ["Marija_prisustvo", "Simona_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    [print(solution) for solution in problem.getSolutions()]
