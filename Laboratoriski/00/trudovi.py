from constraint import *


def has_four(t1, t2, t3, t4, t5, t6, t7, t8, t9, t10):
    termin1 = 0
    termin2 = 0
    termin3 = 0
    termin4 = 0

    termini = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

    for t in termini:
        if t == "T1":
            termin1 += 1
        elif t == "T2":
            termin2 += 1
        elif t == "T3":
            termin3 += 1
        elif t == "T4":
            termin4 += 1

    return termin1 <= 4 and termin2 <= 4 and termin3 <= 4 and termin4 <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())
    variables = []
    for paper in papers:
        variables.append(f'{paper} ({papers[paper]})')
    ai = []
    ml = []
    nlp = []
    for v in variables:
        if "AI" in v:
            ai.append(v)
        elif "ML" in v:
            ml.append(v)
        elif "NLP" in v:
            nlp.append(v)

    if len(ai) <= 4 and len(ai) != 0:
        problem.addConstraint(AllEqualConstraint(), ai)
    if len(ml) <= 4 and len(ml) != 0:
        problem.addConstraint(AllEqualConstraint(), ml)
    if len(nlp) <= 4 and len(nlp) != 0:
        problem.addConstraint(AllEqualConstraint(), nlp)
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(has_four, variables)
    result = problem.getSolution()
    result_sorted = sorted(result)
    tmp = result_sorted[1]
    result_sorted.remove(result_sorted[1])
    result_sorted.append(tmp)
    for p in result_sorted:
        print(f'{p}: {result[p]}')
    # Tuka dodadete go kodot za pechatenje
