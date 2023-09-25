# Small Business Owners in the United States

This code performs various data analysis tasks on a dataset using Python and several libraries. Here's a breakdown of what each section of the code does:

## Libraries
- The required libraries are imported at the beginning of the code, including matplotlib, pandas, seaborn, plotly express, scipy.stats, sklearn.pipeline, sklearn.preprocessing, sklearn.cluster, sklearn.metrics, and sklearn.decomposition.

## Data Loading
- The code loads a CSV file named "SCFP2019.csv.gz" into a pandas DataFrame called `df`. The shape of the DataFrame is printed, and the first few rows of the DataFrame are displayed.

## Business Owners Analysis
- Proportion of business owners in `df` is calculated and stored in the variable `prop_biz_owners`.
- The income categories in `df` are mapped to descriptive labels using the `inccat_dict` dictionary.
- The frequency distribution of income categories for business owners and non-business owners is calculated and stored in the DataFrame `df_inccat`.
- A bar chart is created to visualize the income distribution of business owners and non-business owners using seaborn.

## Home Value Analysis
- A scatter plot is created to compare "Household Debt" and "Home Value" for different types of owners (business/non-business) using seaborn.

## Small Business Owners Analysis
- A subset of `df` is created by filtering small business owners based on income and business owner status.
- A histogram is created to visualize the age distribution of small business owners.

## Variance Analysis
- The top ten variables with the highest variance in the small business owner subset are calculated and stored in the `top_ten_var` variable.
- Trimmed variance is calculated for the top ten variables using the `trimmed_var` function from scipy.stats.
- A horizontal bar chart is created to visualize the top ten variables with the highest trimmed variance using plotly express.

## Clustering Analysis
- A subset of `df` containing the variables with the highest trimmed variance is selected and stored in the `X` variable.
- K-means clustering is performed for different numbers of clusters, and the inertia (sum of squared distances to the nearest centroid) and silhouette score (measure of cluster cohesion and separation) are calculated for each clustering.
- Line plots are created to visualize the relationship between the number of clusters and the inertia and silhouette score respectively using plotly express.

## Final Clustering and PCA
- The final K-means clustering model with a predetermined number of clusters is trained on the `X` dataset.
- The cluster labels are assigned to each data point in `X`, and the mean values of the variables in each cluster are calculated and stored in the `xgb` DataFrame.
- A side-by-side bar chart is created to visualize the mean values of the variables in each cluster using plotly express.
- Principal Component Analysis (PCA) is performed on the `X` dataset to reduce its dimensionality to two components.
- Scatter plot of the two principal components is created to visualize the clusters obtained from K-means clustering using plotly express.

Please note that the code includes saving several images of the generated plots in the "images" directory.

This is a brief overview of the code's functionality. For more detailed information, please refer to the code comments and the documentation of the used libraries.
