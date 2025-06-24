# Age-Adult-ML
# Age to Adult Classifier (Machine Learning)

This project uses logistic regression to classify whether a person is an adult (18 years or older) based on their age. It is a simple binary classification model built using Python, Pandas, NumPy, and Scikit-learn.

## 📌 Features

- Generates synthetic age data (1 to 80 years).
- Labels each person as an adult (1) or not (0).
- Uses logistic regression for classification.
- Visualizes the dataset using Seaborn.
- Splits the dataset into training and testing sets.
- Evaluates the model's performance.

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## 📊 Dataset

Synthetic dataset of 1000 people with:

- Age: Integer (1 to 80)
- Adult: 1 if age >= 18, else 0

## 🔍 Visualization

Scatter plot showing distribution of Age vs Adult using Seaborn.

## 🧠 Model

- Logistic Regression from sklearn.linear_model
- Train-test split: 80% training, 20% testing
- Random state: 42

## 📈 Accuracy

Model accuracy is calculated using .score() function.

## install requried libraries

pip install pandas numpy matplotlib seaborn scikit-learn
