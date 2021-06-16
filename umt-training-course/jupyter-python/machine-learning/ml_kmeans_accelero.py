import os
import pandas as pd
import numpy as np
import sklearn
print("Version de Scikit-Learn :", sklearn.__version__, '\n')
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

chosen_data = ''
while chosen_data != "reduced" and  chosen_data != "full":
    try:
        chosen_data = input('"Reduced" or "full" dataset ? \n\'q\' to quit : ').lower()
        if chosen_data == 'q':
            break
    except:
        print('Please answer "reduced" or "full. Or "q" to quit.')

try:
    csv_file = 'accelero_data_{}.csv'.format(chosen_data)
    print('\nLooking for ', csv_file, '\n')
    df = pd.read_csv(csv_file, sep=',', parse_dates=['date'])
    print(df.head(), '\n')
except:
    print('\n ** Could not open csv file **')

X = df[df.columns[-3:]]
Y = df['position']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle=True, random_state=0, stratify=Y)

parameters = [{
    'n_neighbors': range(2, 26)
}]

grid_search = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid=parameters,
    scoring='accuracy',
    cv=5,
    n_jobs=-1,
    verbose=9
)

grid_search.fit(X_train, Y_train)

best_model = grid_search.best_estimator_

print('\nMeilleur modèle retenu : ', best_model)

Y_predict_train = best_model.predict(X_train)
print("\nScore du modèle sur l\'apprentissage : ", accuracy_score(Y_train, Y_predict_train) * 100, ' %')
print(classification_report(Y_train, Y_predict_train))
cm_train = confusion_matrix(Y_train, Y_predict_train)
print(cm_train)

Y_predict_test = best_model.predict(X_test)
print("\nScore du modèle sur le test : ", accuracy_score(Y_test, Y_predict_test) * 100, ' %')
print(classification_report(Y_test, Y_predict_test))
cm_test = confusion_matrix(Y_test, Y_predict_test)
print(cm_test)

joblib.dump(best_model, 'kmeans_accelero_reduced.joblib')
print('\nModel saved as \'kmeans_accelero_reduced.joblib\'\n')