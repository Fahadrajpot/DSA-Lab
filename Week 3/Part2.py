import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = pd.read_csv('Test.csv')

    symptoms = data.columns[:-1]
    label = data.columns[-1]

    fig, axes = plt.subplots(nrows=int(np.ceil(len(symptoms) / 5)), ncols=5, figsize=(20, 10))
    fig.suptitle('Relationship between Each Symptom and Labels', fontsize=16)

    axes = axes.flatten()

    for idx, symptom in enumerate(symptoms):
        axes[idx].scatter(data[symptom], data[label], alpha=0.5)
        axes[idx].set_title(symptom)
        axes[idx].set_xlabel(symptom)
        axes[idx].set_ylabel(label)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    for idx in range(len(symptoms), len(axes)):
        axes[idx].set_visible(False)

    plt.show()

    train_data = data.sample(frac=0.8, random_state=25)
    test_data = data.drop(train_data.index)

    test_data['Predicted Label'] = np.nan

    test_point = test_data.iloc[0, :-1]
    distances = train_data.apply(lambda row: euclidean_distance(row[:-1], test_point), axis=1)
    test_data.at[test_data.index[0], 'Predicted Label'] = train_data.iloc[distances.idxmin(), -1]

    accuracy = classify_and_calculate_accuracy(test_data, train_data)
    print(f'Accuracy: {accuracy:.2f}%')

    print("Time complexity for classifying each test sample is O(n*m).")

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def classify_and_calculate_accuracy(test_data, train_data):
    predictions = []
    for index, test_row in test_data.iterrows():
        distances = train_data.apply(lambda train_row: euclidean_distance(train_row[:-1], test_row[:-1]), axis=1)
        predicted_label = train_data.iloc[distances.idxmin(), -1]
        predictions.append(predicted_label)
    test_data['Predicted Label'] = predictions
    accuracy = (test_data['Predicted Label'] == test_data[label]).mean() * 100
    return accuracy

if __name__ == "__main__":
    main()