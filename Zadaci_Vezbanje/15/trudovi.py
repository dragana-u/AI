from constraint import *


def only_four(tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10):
    term1 = 0
    term2 = 0
    term3 = 0
    term4 = 0

    terms = [tr1, tr2, tr3, tr4, tr5, tr6, tr7, tr8, tr9, tr10]

    for term in terms:
        if term == "T1":
            term1 += 1
        if term == "T2":
            term2 += 1
        if term == "T3":
            term3 += 1
        if term == "T4":
            term4 += 1
    return term1 <= 4 and term2 <= 4 and term3 <= 4 and term4 <= 4


if __name__ == '__main__':
    num = int(input())

    papers = dict()

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()

    # Tuka definirajte gi promenlivite
    ai = []
    ml = []
    nlp = []
    domain = [f'T{i + 1}' for i in range(num)]
    i = 1
    for item in papers.items():
        if item.__contains__("AI"):
            ai.append(f'Paper{i} (AI):')
        elif item.__contains__("ML"):
            ml.append(f'Paper{i} (ML):')
        elif item.__contains__("NLP"):
            nlp.append(f'Paper{i} (NLP):')
        i += 1
    problem = Problem(BacktrackingSolver())
    variables = ai + ml + nlp
    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)
    # Tuka dodadete gi ogranichuvanjata
    if len(ai) <= 4 and len(ai) != 0:
        problem.addConstraint(AllEqualConstraint(), ai)
    if len(ml) <= 4 and len(ml) != 0:
        problem.addConstraint(AllEqualConstraint(), ml)
    if len(nlp) <= 4 and len(nlp) != 0:
        problem.addConstraint(AllEqualConstraint(), nlp)

    problem.addConstraint(only_four, variables)

    result = problem.getSolution()
    result_sorted = sorted(result)
    tmp = result_sorted[1]
    result_sorted.remove(result_sorted[1])
    result_sorted.append(tmp)
    for r in result_sorted:
        print(f'{r} {result[r]}')
    # Tuka dodadete go kodot za pechatenje
