import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score,classification_report
from allComp_data_prep import data
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV

X=data.drop('comp_id',axis=1)
y=data['comp_id']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

xgb_clf = xgb.XGBClassifier(
    objective='multi:softmax',
    eval_metric='mlogloss',
    random_state=101,
    device='cpu',
    n_jobs=1,
)
param_grid = {
    'n_estimators': [100, 200, 500],
    'learning_rate': [0.01, 0.1],
    'reg_alpha': [0.0, 0.1, 0.2],
    'reg_lambda': [0.1, 0.2, 0.3],
    'subsample': [0.5, 0.7, 0.8],
    'gamma': [0.1, 0.2, 0.5, 1],
}

search = RandomizedSearchCV(
    estimator=xgb_clf,
    param_distributions=param_grid,
    n_iter=60,
    scoring='roc_auc_ovr',
    cv=4,
    n_jobs=-1,
    random_state=101,
    verbose=2,
    refit=True,
)

search.fit(X_train, y_train)


print("Best params:", search.best_params_)
print("Best CV score:", search.best_score_)

# Evaluate on test set
best_model = search.best_estimator_
y_pred = best_model.predict(X_test)
print("\nTest accuracy:", accuracy_score(y_test, y_pred))
print("\n", classification_report(y_test, y_pred))

from joblib import dump, load
dump(best_model, 'base_comp_model.joblib')
