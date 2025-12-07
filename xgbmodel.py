import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay

alz = pd.read_csv("alzheimers_disease_data.csv")
alz = alz.drop(columns = ['PatientID','Ethnicity', 'DoctorInCharge'])

cat_col = alz.select_dtypes(include = 'object')

num_col = alz.select_dtypes(include = ['int64', 'float64'])

num_col = alz.drop(columns = ['Diagnosis'])

categorical_features = []

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OrdinalEncoder(
        handle_unknown='use_encoded_value',
        unknown_value=-1
    ))
])

numerical_features = ['Age', 'Gender', 'EducationLevel', 'BMI', 'Smoking',
       'AlcoholConsumption', 'PhysicalActivity', 'DietQuality', 'SleepQuality',
       'FamilyHistoryAlzheimers', 'CardiovascularDisease', 'Diabetes',
       'Depression', 'HeadInjury', 'Hypertension', 'SystolicBP', 'DiastolicBP',
       'CholesterolTotal', 'CholesterolLDL', 'CholesterolHDL',
       'CholesterolTriglycerides', 'MMSE', 'FunctionalAssessment',
       'MemoryComplaints', 'BehavioralProblems', 'ADL', 'Confusion',
       'Disorientation', 'PersonalityChanges', 'DifficultyCompletingTasks',
       'Forgetfulness']
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler()),                   
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='drop'
)

xgb = GradientBoostingClassifier(n_estimators=100, max_depth=3, random_state=42)

model_gbx = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', xgb)
])

final_columns = categorical_features + numerical_features + ['Diagnosis']
alz_preprocessed = pd.DataFrame(alz, columns = final_columns)

X = alz_preprocessed.drop(columns='Diagnosis', axis = 1)
y = alz_preprocessed['Diagnosis']

X_train,X_test, y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_gbx.fit(X_train,y_train)

result = model_gbx.predict(X_test)

xgb_cof_metrix = confusion_matrix(y_test, result)
xgb_cm = xgb_cof_metrix.ravel()
tp = xgb_cm[0]
fp = xgb_cm[1]
fn = xgb_cm[2]
tn = xgb_cm[3]
print('True Positive:', tp)
print('False Positive:', fp)
print('False Negative:', fn)
print('True Negative:', tn)

xgb_accuracy_score_value = (tp+tn)/(tp+tn+fp+fn)
xgb_precision = tp/(tp+fp)
xgb_recall = tp / (tp+fn)
xgb_f1_score = 2 * ((xgb_precision*xgb_recall)/ (xgb_precision+xgb_recall))
print('Accuracy Score:', xgb_accuracy_score_value)
print('Precision:', xgb_precision)
print('Recall:', xgb_recall)
print('f1 Score:', xgb_f1_score)

import pickle
with open('xgbmodel.pkl', 'wb') as f:
    pickle.dump(xgb,f)
