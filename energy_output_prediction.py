import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with your actual dataset path

# Display the first few rows of the dataset
print(data.head())

# Split the data into features (X) and target variable (y)
X = data.drop(columns=['PE'])  # Features: all columns except 'PE'
y = data['PE']  # Target variable: 'PE'

# Split the data into training and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Linear Regression
linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
linear_reg_predictions = linear_reg.predict(X_test)

# Model 2: Random Forest Regressor
random_forest = RandomForestRegressor(n_estimators=100, random_state=42)
random_forest.fit(X_train, y_train)
random_forest_predictions = random_forest.predict(X_test)

# Evaluate models
linear_reg_mse = mean_squared_error(y_test, linear_reg_predictions)
random_forest_mse = mean_squared_error(y_test, random_forest_predictions)

# Print model evaluation metrics
print(f"Linear Regression MSE: {linear_reg_mse}")
print(f"Random Forest Regressor MSE: {random_forest_mse}")

# Visualize predictions vs actual values for Random Forest model
plt.scatter(y_test, random_forest_predictions, alpha=0.5)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Random Forest Regressor: Actual vs Predicted')
plt.show()
