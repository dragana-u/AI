import os
from sklearn.naive_bayes import GaussianNB

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    data = []
    for row in dataset:
        r = [float(el) for el in row[:-1]]
        r.append(int(row[-1]))
        data.append(r)
    dataset = data
    splitting = int(0.85 * len(dataset))
    train_set = dataset[:splitting]
    train_X = [red[:-1] for red in train_set]
    train_Y = [red[-1] for red in train_set]

    test_set = dataset[splitting:]
    test_X = [red[:-1] for red in test_set]
    test_Y = [red[-1] for red in test_set]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    preciznost = 0
    for t in range(len(test_set)):
        predicted = classifier.predict([test_X[t]])[0]
        true_class = test_Y[t]
        if predicted == true_class:
            preciznost += 1

    preciznost = preciznost / len(test_set)
    print(preciznost)

    vlez = [float(el) for el in input().split(" ")]
    predicted_vlez = classifier.predict([vlez])[0]
    print(predicted_vlez)
    verojatnost = classifier.predict_proba([vlez])
    print(verojatnost)
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *
