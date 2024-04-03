# -*- coding: utf-8 -*-
"""Onspotquiz1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w7v0-vTyfTpTMsZrMo4ZU-DtdR7jnWE6
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv("/content/DSAI-LVA-DATASET for Quiz.csv")
data = pd.DataFrame(data)


label_encoder = LabelEncoder()
data['ParentEducation'] = label_encoder.fit_transform(data['ParentEducation'])
data['Pass'] = label_encoder.fit_transform(data['Pass'])


X = data[['StudyTime', 'PreviousTestScore', 'ParentEducation']]
y = data['Pass']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))


for index, student in X_test.iterrows():
    prediction = classifier.predict(student.values.reshape(1, -1))
    pass_s = label_encoder.inverse_transform(prediction)[0]

    probabilities = classifier.predict_proba(student.values.reshape(1, -1))
    pass_threshold = 0.5

    if probabilities[0][1] >= pass_threshold:
        classification = "Pass"
    else:
        classification = "Fail"


    if pass_s == 1:
        previous_test_score = student['PreviousTestScore']
        if previous_test_score >= 85:
            grade = "High Grade"
        else:
            grade = "Low Grade"
    else:
        grade = "Fail"

    print(f"Student {index}: Pass status: {pass_s},grade : {grade}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import warnings
warnings.filterwarnings('ignore')


data = pd.read_csv("/content/DSAI-LVA-DATASET for Quiz.csv")
data = pd.DataFrame(data)


label_encoder = LabelEncoder()
data['ParentEducation'] = label_encoder.fit_transform(data['ParentEducation'])
data['Pass'] = label_encoder.fit_transform(data['Pass'])


X = data[['StudyTime', 'PreviousTestScore', 'ParentEducation']]
y = data['Pass']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


classifier = RandomForestClassifier(random_state=42)
classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
print("Classification Report:")
print(classification_report(y_test, y_pred))


for index, student in X_test.iterrows():
    pred = classifier.predict(student.values.reshape(1, -1))
    pass_s = label_encoder.inverse_transform(pred)

    print(pass_s)
    if pass_s == ['Yes']:
        previous_test_score = data['PreviousTestScore']
        if previous_test_score >= 85:
            grade = "High Grade"
        else:
            grade = "Low Grade"
    else:
        grade = "Fail"

    # print(f"Student {index}: Pass status: {pass_s}, Grade: {grade}")

import pandas as pd

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/DSAI-LVA-DATASET for Quiz.csv")
print(len(data))

# Split the data into train and test sets (e.g., 80% train, 20% test)
train_data = data.sample(frac=0.8)  # Use 80% of the data for training
test_data = data.drop(train_data.index)  # Use the remaining data for testing

# Save the train and test sets to separate CSV files
train_data.to_csv("train_data.csv", index=False)
test_data.to_csv("test_data.csv", index=False)

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load train data from CSV
train_data = pd.read_csv("train_data.csv")

# Load test data from CSV
test_data = pd.read_csv("test_data.csv")

# Fill missing values with mean and drop duplicates for train data
train_data = train_data.fillna(train_data.mean())
train_data = train_data.drop_duplicates()

# Fill missing values with mean and drop duplicates for test data
test_data = test_data.fillna(test_data.mean())
test_data = test_data.drop_duplicates()

# Apply one-hot encoding to categorical columns in train and test data
train_data = pd.get_dummies(train_data, columns=['ParentEducation', 'Pass'])
test_data = pd.get_dummies(test_data, columns=['ParentEducation', 'Pass'])

# Separate features and target variable for train and test data
X_train = train_data.drop(columns=['Pass_No','Pass_Yes' ])  # Features for training
y_train = train_data[['Pass_No', 'Pass_Yes']]  # Target variable for training
X_test = test_data.drop(columns=['Pass_No','Pass_Yes'])  # Features for testing
y_test = test_data[['Pass_No', 'Pass_Yes']]  # Target variable for testing

# Initialize and train Decision Tree classifier
decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)

# Predict on test data
y_pred = decision_tree.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Decision Tree Classifier Accuracy:", accuracy)

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import random
# Load the dataset
data = pd.read_csv('DSAI-LVA-DATASET for Quiz.csv')

data.head()

data.info()

parent_education_mapping = {
    'HighSchool': np.random.choice(['HighSchool', 'College'], size=len(data)),
    'College': np.random.choice(['Masters', 'Bachelors'], size=len(data))
}
data['ParentEducation'] = data['ParentEducation'].map(lambda x: np.random.choice(parent_education_mapping[x]))

def categorize_score(pass_status, score):
    if pass_status == 'Yes' and score >= 90:
        return 1
    elif pass_status == 'Yes' and score < 90:
        return 2
    elif pass_status == 'No':
        return 3
    else:
        return np.nan

data['Pass'] = data.apply(lambda row: categorize_score(row['Pass'], row['PreviousTestScore']), axis=1)

print(data)

label_encoder = LabelEncoder()
data['ParentEducation'] = label_encoder.fit_transform(data['ParentEducation'])

print(data)

total_rows = len(data)
train_rows = int(0.8 * total_rows)
test_rows = total_rows - train_rows

# Shuffle the DataFrame to ensure randomness
data_shuffled = data.sample(frac=1, random_state=42)

# Split the DataFrame into training and testing subsets
train_data = data_shuffled.iloc[:train_rows]
test_data = data_shuffled.iloc[train_rows:]

# Write training and testing data to CSV files
train_data.to_csv('/content/sample_data/train_data.csv', index=False)
test_data.to_csv('/content/sample_data/test_data.csv', index=False)

import xgboost as xgb

train_data = pd.read_csv('/content/sample_data/train_data.csv')
test_data = pd.read_csv('/content/sample_data/test_data.csv')

train_data['Pass'] = label_encoder.fit_transform(train_data['Pass'])
test_data['Pass'] = label_encoder.fit_transform(test_data['Pass'])
# Define X and y for training and testing data
X_train = train_data.drop('Pass', axis=1)
y_train = train_data['Pass']
X_test = test_data.drop('Pass', axis=1)
y_test = test_data['Pass']

# Model Engineering
models = {
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'XGBoost': xgb.XGBClassifier()  # XGBoost added
}

results = {}

for name, model in models.items():
    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Model evaluation
    accuracy = accuracy_score(y_test, y_pred)
    results[name] = accuracy

    print(f"Model: {name}")
    print(f"Accuracy: {accuracy:.2f}")
    print(classification_report(y_test, y_pred))
    print(confusion_matrix(y_test, y_pred))
    print("="*50)

# Model comparison
print("Model Comparison:")
for name, accuracy in results.items():
    print(f"{name}: {accuracy:.2f}")

# Visualization
# Confusion Matrix
plt.figure(figsize=(12, 8))
for i, (name, model) in enumerate(models.items()):
    plt.subplot(2, 3, i+1)
    sns.heatmap(confusion_matrix(y_test, model.predict(X_test)), annot=True, fmt="d", cmap="Blues")
    plt.title(name)
plt.tight_layout()
plt.show()

# Write model comparison and outcome to a file
with open('model_comparison.txt', 'w') as f:
    f.write("Model Comparison:\n")
    for name, accuracy in results.items():
        f.write(f"{name}: {accuracy:.2f}\n")



import pandas as pd
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, precision_score, f1_score, recall_score
import time

mark_df = pd.read_csv('/content/DSAI-LVA-DATASET for Quiz.csv')
print(mark_df.head())

for i, rows in mark_df.iterrows():
    if rows['Pass'] == 'Yes' and rows['PreviousTestScore'] >= 75:
        mark_df.loc[i, 'Result'] = 'HGPass'
    elif rows['Pass'] == 'Yes' and rows['PreviousTestScore'] < 75:
        mark_df.loc[i, 'Result'] = 'LGPass'
    elif rows['Pass'] == 'No':
        mark_df.loc[i, 'Result'] = 'Fail'
mark_df = mark_df.drop('Pass', axis=1)

print(mark_df.head())

parent_edu = ['Masters', 'Bachelor''s', 'College', 'High School', 'Not Educated']
mark_df['Parent_Education'] = np.random.choice(parent_edu, size = len(mark_df['StudyTime']))

mark_df = mark_df.drop('ParentEducation', axis=1)
print(mark_df.head())

mark_df_shuffled = mark_df.sample(frac=1, random_state=42).reset_index(drop=True)

train_size = int(0.7 * len(mark_df_shuffled))

train_set = mark_df_shuffled.iloc[:train_size]
test_set = mark_df_shuffled.iloc[train_size:]

train_set.to_csv('train.csv', index=False)
test_set.to_csv('test.csv', index=False)

test_df=pd.read_csv('/content/test.csv')
train_df=pd.read_csv('/content/train.csv')

lbl = LabelEncoder()
train_df['Parent_Education'] = lbl.fit_transform(train_df['Parent_Education'])
test_df['Parent_Education'] = lbl.transform(test_df['Parent_Education'])
train_df['Result'] = lbl.fit_transform(train_df['Result'])
test_df['Result'] = lbl.transform(test_df['Result'])

X_train = train_df.drop('Result', axis=1)
X_test = test_df.drop('Result', axis=1)
y_train = train_df['Result']
y_test = test_df['Result']

model_name = [
    ('Decision Tree Classifier', DecisionTreeClassifier()),
    ('K Nearest Neighbors', KNeighborsClassifier(n_neighbors=2)),
    ('SVM', SVC()),
    ('XGB Classifier', XGBClassifier(learning_rate=0.01, gamma=3))
]

results = {}
for name, model in model_name:
    start_time = time.time()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    time_taken = round((time.time() - start_time), 2)
    accuracy = accuracy_score(y_pred, y_test)
    results[name] = accuracy
    print(f'{name} \nAccuracy : {accuracy*100:.2f}% \nTime Taken: {time_taken} sec\n ')

# Plotting the results
model_plot = pd.DataFrame(results.values(), index=results.keys(), columns=['Accuracy'])
model_plot.plot(kind='barh')
plt.xlabel('Accuracy')
plt.title('Model Accuracy Comparison')
plt.show()