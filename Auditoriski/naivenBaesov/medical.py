import csv

from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    dataset_v2 = []
    for row in dataset:
        row_v2 = [int(el) for el in row]
        dataset_v2.append(row_v2)

    return dataset_v2


if __name__ == '__main__':
    dataset = read_file('medical.csv')
    # treniranje i testiranje
    train_set = dataset[:int(0.75*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.75*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_x)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy/len(test_set)
    acc = accuracy_score(test_y, classifier.predict(test_x))
    print(f'Accuracy: {accuracy}')
    print(acc)
    entry = [int(el) for el in input().split(' ')]
    predicted_class = classifier.predict([entry])[0]
    print(predicted_class)
    print(classifier.predict_proba([entry]))
