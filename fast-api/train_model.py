import joblib, json

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, accuracy_score, recall_score, confusion_matrix

meta = {
    "n_features": 3,
    "n_classes": 4

}
X, y = make_classification(
    n_samples = 15000, 
    n_features = meta['n_features'], 
    n_informative = meta['n_features'],
    n_redundant = 0,
    n_classes = meta['n_classes'],    
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=997)

pipeline = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('rf', RandomForestClassifier(
        n_estimators=45, 
        criterion='entropy', 
        n_jobs=-1)
    )
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

f1 = f1_score(y_test, y_pred, average="weighted")

print(f'F1 Score: {f1:.4f}')

joblib.dump(pipeline, 'model/model.joblib')
print('Model saved')

meta['model_name'] = type(pipeline.named_steps['rf']).__name__
meta['f1_score'] = f1

with open('meta.json', 'w') as fp:
    json.dump(meta, fp)

print('Saved metadata')
print('Goodbye')
