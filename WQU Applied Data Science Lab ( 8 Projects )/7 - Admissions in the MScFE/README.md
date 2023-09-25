# Admissions in the MScFE

This README file provides an overview of the code and its functionality. The code performs various operations related to data analysis and experimentation using MongoDB and Python libraries. Here's a breakdown of the code:

## Setup

The initial part of the code sets up the necessary imports and configurations. It imports the required libraries and initializes the `wqet_grader` for assessment purposes. It also resets the MongoDB database using the `Reset` class from `teaching_tools.ab_test.reset`.

## Data Aggregation and Analysis

The code performs data aggregation and analysis using MongoDB queries and pandas operations.

1. Aggregating Applicants by Nationality:
   - The code aggregates the applicants by nationality using a MongoDB aggregation pipeline.
   - The result is loaded into a pandas DataFrame called `df_nationality` for further processing.
   - The DataFrame includes columns for country ISO codes, country names, and applicant counts.

2. Creating a Choropleth Map:
   - The code defines a function called `build_nat_choropleth` to create a choropleth map using the `plotly.express` library.
   - The function uses the `df_nationality` DataFrame to plot the map, representing the percentage of applicants from each country.

3. MongoDB Repository Class:
   - The code defines a class called `MongoRepository` that acts as a repository for interacting with a MongoDB database.
   - The class provides methods for finding applicants by date, updating applicants, assigning applicants to groups, and finding experimental observations.

4. Power Calculation:
   - The code uses the `GofChisquarePower` class from `statsmodels.stats.power` to calculate the group size needed for a chi-square test.
   - The calculated group size is printed as output.

5. Aggregating No-Quiz Applicants by Sign-Up Date:
   - The code aggregates the number of no-quiz applicants by sign-up date using a MongoDB aggregation pipeline.
   - The result is loaded into a pandas Series called `no_quiz_mscfe` for further analysis.

6. Statistical Analysis:
   - The code performs statistical analysis on the aggregated data, including calculating the mean and standard deviation.
   - It then calculates the mean and standard deviation for a specified number of experimental days.
   - Finally, it calculates and prints the probability of achieving a certain number of no-quiz applicants within the specified experimental days.

7. Experimentation:
   - The code uses the `Experiment` class from `teaching_tools.ab_test.experiment` to run an experiment.
   - The experiment involves assigning applicants to control and treatment groups based on a specified date.
   - The result of the experiment is printed as output.

8. Analyzing Experimental Observations:
   - The code retrieves the experimental observations from the MongoDB database.
   - The observations are loaded into a pandas DataFrame called `df` for further analysis.
   - The DataFrame is used to create a contingency table and a side-by-side bar chart using the `plotly.express` library.
   - The contingency table and the result of the chi-square test are printed as output.
   - The odds ratio is also calculated and printed as output.

## Usage

To use this code, make sure you have the required libraries installed and a MongoDB server running on `localhost` with the default port `27017`. You can modify the MongoDB connection settings in the code if needed.

Ensure that you have the necessary data in the MongoDB database and adjust the code accordingly to match your data schema and collection names.

The code can be executed as a script or run interactively in a Python environment. Each section of the code is commented and provides explanations for its purpose and functionality.

Please note that this README file provides a summary of the code's functionality. For a more detailed understanding, refer to the code comments and consult the documentation of the imported libraries for further information.
