# 📏 Height Predictor (R² 86%+)

This project is a high-accuracy Height Prediction system built using **Scikit-Learn** and deployed via **Streamlit**. By leveraging **Polynomial Regression** and including **Gender** as a key feature, the model achieves a precision of over 86%.

## 🚀 Overview
Predicting human height based only on weight often leads to lower accuracy (~75%) because body types vary significantly by gender and follow non-linear growth patterns. This project solves that by:
1.  **Feature Engineering**: Including Gender (Male/Female) to account for biological differences.
2.  **Polynomial Transformation**: Using `degree=2` to capture the non-linear relationship between weight and height.
3.  **Deployment**: A clean, interactive web interface built with Streamlit.

## 📊 Dataset
The model is trained on the [Kaggle Weight-Height Dataset](https://www.kaggle.com/datasets/mustafaali96/weight-height) containing 10,000 records.
-   **Original Units**: Inches and Pounds.
-   **Processing**: The system automatically converts data to the Metric system (**cm** and **kg**) for user convenience.

## 🛠️ Tech Stack
-   **Python 3.x**
-   **Scikit-Learn**: For the Machine Learning Pipeline (PolynomialFeatures, StandardScaler, LinearRegression).
-   **Pandas/Numpy**: For data manipulation.
-   **Streamlit**: For the web-based UI.
-   **Pickle**: For model serialization.

## 📁 Project Structure
- `SimpleLinearRegression.ipynb`: The notebook where the model was researched and trained.
- `weight-height.csv`: The raw dataset.
- `height_predictor_pipeline.pkl`: The exported model (includes scaling and polynomial logic).
- `app.py`: The Streamlit application script.
- `README.md`: This file.

## ⚙️ Installation & Usage

1. **Clone the repository or download the files.**
2. **Install dependencies**:
   ```bash
   pip install pandas scikit-learn streamlit