{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58bf0f0f-a31f-4343-a3ba-d8da197c17ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "data = pd.read_csv('titanic.csv')\n",
    "\n",
    "data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)\n",
    "data['Age'].fillna(data['Age'].median(), inplace=True)\n",
    "data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)\n",
    "\n",
    "data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)\n",
    "\n",
    "X = data.drop('Survived', axis=1)\n",
    "y = data['Survived']\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "model = LogisticRegression()\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "y_pred = model.predict(X_test)\n",
    "accuracy = accuracy_score(y_test, y_pred)\n",
    "print(\"Accuracy:\", accuracy)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
