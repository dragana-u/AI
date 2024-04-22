import os
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
           ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
           ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    encoder = OrdinalEncoder()
    encoder.fit([red[:-1] for red in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [red[:-1] for red in train_set]
    train_Y = [red[-1] for red in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [red[:-1] for red in test_set]
    test_Y = [red[-1] for red in test_set]
    test_X = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    preciznost = 0
    for t in range(len(test_set)):
        predicted_class = classifier.predict([test_X[t]])[0]
        true_class = test_Y[t]
        if predicted_class == true_class:
            preciznost += 1
    preciznost = preciznost / len(test_set)
    print(preciznost)
    vlez = [el for el in input().split(" ")]
    encoded_vlez = encoder.transform([vlez])
    predicted_vlez = classifier.predict(encoded_vlez)[0]
    print(predicted_vlez)
    verojatnost = classifier.predict_proba(encoded_vlez)
    print(verojatnost)
# Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
# klasifikatorot i encoderot so povik na slednite funkcii

# submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

# submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

# submit na klasifikatorot
    submit_classifier(classifier)

# submit na encoderot
    submit_encoder(encoder)

# povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *
