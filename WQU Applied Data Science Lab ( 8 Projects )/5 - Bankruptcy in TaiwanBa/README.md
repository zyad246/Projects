# Bankruptcy Prediction in Taiwan

This repository contains code for performing bankruptcy prediction in Taiwan using a random forest classifier. The code utilizes a dataset stored in a JSON file and performs data preprocessing, model training, hyperparameter tuning, and evaluation.

## Usage Guidelines

Please ensure that you have the necessary dependencies installed to run this code. It is recommended to use a Python environment with the required libraries such as pandas, scikit-learn, imblearn, matplotlib, and pickle.

## Code Description

The code performs the following steps:

1. **Data Loading**: The code imports the necessary libraries (`gzip`, `json`, `pickle`, `matplotlib`, `pandas`, `imblearn`, `sklearn`) and loads the bankruptcy dataset from a compressed JSON file (`data/taiwan-bankruptcy-data.json.gz`) using the `gzip` and `json` modules. The loaded data is stored in the `taiwan_data` variable.

2. **Data Wrangling**: The code defines a `wrangle` function that reads the JSON data, converts it to a pandas DataFrame, and sets the "id" column as the index. The `wrangle` function is then used to create a DataFrame (`df`) containing the bankruptcy data.

3. **Data Exploration**: The code explores the loaded dataset by displaying information such as the shape of the DataFrame, the count of missing values for each column, and the class balance of the target variable ("bankrupt"). Additionally, a bar plot is generated to visualize the distribution of the target variable.

4. **Data Preprocessing**: The code prepares the data for model training by splitting it into features (`X`) and the target variable (`y`). Further, the data is split into training and testing sets using the `train_test_split` function from scikit-learn. To address class imbalance, the training data is oversampled using the `RandomOverSampler` from the imblearn library.

5. **Model Training**: The code initializes a `RandomForestClassifier` and fits it to the oversampled training data. Cross-validation is performed using the `cross_val_score` function to assess the model's performance.

6. **Hyperparameter Tuning**: The code defines a parameter grid (`params`) for the `RandomForestClassifier` and performs a grid search using the `GridSearchCV` function to find the best combination of hyperparameters.

7. **Model Evaluation**: The code evaluates the trained model on both the training and testing data by calculating the accuracy scores. Additionally, a confusion matrix is generated to visualize the model's performance on the testing data.

8. **Feature Importance**: The code calculates the feature importances using the best estimator from the grid search and visualizes the top 10 important features.

9. **Model Saving**: The code saves the trained and tuned model using the `pickle` module. The model is stored in a file named `model-5-5.pkl`.

10. **Predictions**: The code imports a custom module `my_predictor_assignment.py` and generates predictions on a separate test dataset using the trained model. The predictions are stored in the `y_test_pred` variable.

## License

This code does not include any specific license information. Please refer to the guidelines and restrictions mentioned in the "Usage Guidelines" section.

## Disclaimer

The code and information in this repository are for educational purposes only. They do not constitute financial or legal advice. Use the code and analysis at your own risk and discretion.
