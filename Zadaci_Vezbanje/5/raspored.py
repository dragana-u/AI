from constraint import *


def ML_different_time_slot(slot_1, slot_2):
    slot_1 = slot_1.split("_")
    slot_2 = slot_2.split("_")
    return slot_1[1] != slot_2[1]

def two_hour_class(slot_1, slot_2):
    slot_1 = slot_1.split("_")
    slot_2 = slot_2.split("_")
    if slot_1[0] == slot_2[0]:
        slot_1[1] = int(slot_1[1])
        slot_2[1] = int(slot_2[1])
        if slot_1[1] == slot_2[1]:
            return False
        if slot_1[1] + 1 == slot_2[1]:
            return False
        if slot_1[1] == slot_2[1] + 1:
            return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_casovi = []
    ML_casovi = []
    R_casovi = []
    BI_casovi = []

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    for i in range(1, casovi_AI + 1):
        AI_casovi.append(f'AI_cas_{i}')
    for i in range(1, casovi_R + 1):
        R_casovi.append(f'R_cas_{i}')
    for i in range(1, casovi_BI + 1):
        BI_casovi.append(f'BI_cas_{i}')
    for i in range(1, casovi_ML + 1):
        ML_casovi.append(f'ML_cas_{i}')

    problem.addVariables(AI_casovi, AI_predavanja_domain)
    problem.addVariables(ML_casovi, ML_predavanja_domain)
    problem.addVariables(R_casovi, R_predavanja_domain)
    problem.addVariables(BI_casovi, BI_predavanja_domain)

    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    # ---Tuka dodadete gi ogranichuvanjata----------------
    # ----------------------------------------------------
    all_time_slots = AI_casovi + BI_casovi + ML_casovi + R_casovi + ["AI_vezbi", "ML_vezbi", "BI_vezbi"]
    problem.addConstraint(AllDifferentConstraint(), all_time_slots)
    all_ML = ML_casovi + ["ML_vezbi"]
    for slot1 in all_ML:
        for slot2 in all_ML:
            if slot1 != slot2:
                problem.addConstraint(ML_different_time_slot, [slot1, slot2])

    for slot1 in all_time_slots:
        for slot2 in all_time_slots:
            if slot1 != slot2:
                problem.addConstraint(two_hour_class,[slot1, slot2])

    solution = problem.getSolution()
    print(solution)
