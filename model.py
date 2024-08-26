import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("review.csv")

# Create a TfidfVectorizer object
vectorizer = TfidfVectorizer(stop_words="english")

# Transform the reviews into TF-IDF vectors
X = vectorizer.fit_transform(df["text"])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, df["label"], test_size=0.25, random_state=42)

# Create a logistic regression model
clf = LogisticRegression()

# Train the model on the training data
clf.fit(X_train, y_train)
# Evaluate the model on the testing data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = np.mean(y_pred == y_test)

print("Accuracy:", accuracy)

