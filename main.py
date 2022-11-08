# roc curve and roc auc on an imbalanced dataset
from sklearn.datasets import make_classification
from sklearn.dummy import DummyClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

aucs = []
n_folds = 10
n_samples = 10_000

for strategy in ("most_frequent", "uniform", "prior"):
    print(f"--- Strategy: {strategy} ---")
    for minority_class_prevalence in (0.1, 0.01, 0.001, 0.0001, 0.00001):
        for i in range(0, n_folds):
            # Generate 2 class dataset
            X, y = make_classification(
                n_samples=n_samples,
                n_classes=2,
                weights=[1 - minority_class_prevalence, minority_class_prevalence],
                random_state=i,
            )

            # Split into train/test sets with same class ratio
            trainX, testX, trainy, testy = train_test_split(
                X, y, test_size=0.5, random_state=i, stratify=y
            )

            # Naive models
            model = DummyClassifier(strategy=strategy)
            model.fit(trainX, trainy)
            yhat = model.predict_proba(testX)

            naive_probs = yhat[:, 1]

            # calculate roc auc
            roc_auc = roc_auc_score(testy, naive_probs)
            aucs += [roc_auc]

        # Force minority_class_prevalence to be a float with at least 5 decimals
        minority_class_prevalence = f"{minority_class_prevalence:.5f}"

        print(
            f"Prevalence: {minority_class_prevalence} | AUC: {round(sum(aucs)/len(aucs), 4)}"
        )
