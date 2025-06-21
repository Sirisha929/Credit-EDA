# 🧾 Credit EDA Project

This project performs **Exploratory Data Analysis (EDA)** on a credit dataset to uncover patterns and insights related to credit risk. It includes cleaning, visualization, and transformation of data to prepare for future modeling like credit scoring or loan approval prediction.

## 📌 Objective

To analyze customer financial data and understand the key factors that affect **loan defaults** using Python libraries like `pandas`, `matplotlib`, and `seaborn`.

---

## 🧪 Key Features

- Data Cleaning (missing values, duplicates)
- Univariate, Bivariate, and Multivariate Analysis
- Visualizations using histograms, boxplots, heatmaps, scatter plots
- Correlation and distribution analysis
- Data Transformation (Log Transform, Scaling)

---

## 📂 Project Structure

📁 Credit_EDA_Project
│
├── credit_data.csv # Sample dataset used for analysis
├── Credit.py # Python script version of the analysis
└── README.md # Project documentation

---



Output:  
First 5 Rows:
   customer_id  age  gender  ...  dependents    purpose  defaulted
0        C001   59  Female  ...           2   Business          0
1        C002   49    Male  ...           2  Education          0
2        C003   35    Male  ...           2   Business          0
3        C004   63    Male  ...           3        Car          0
4        C005   28  Female  ...           1       Home          1

[5 rows x 14 columns]
Data Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 200 entries, 0 to 199
Data columns (total 14 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   customer_id      200 non-null    object
 1   age              200 non-null    int64 
 2   gender           200 non-null    object
 3   income           200 non-null    int64 
 4   loan_amount      200 non-null    int64 
 5   loan_term        200 non-null    int64 
 6   credit_score     200 non-null    int64 
 7   employment_type  200 non-null    object
 8   marital_status   200 non-null    object
 9   education        200 non-null    object
 10  residence_type   200 non-null    object
 11  dependents       200 non-null    int64 
 12  purpose          200 non-null    object
 13  defaulted        200 non-null    int64 
dtypes: int64(7), object(7)
memory usage: 22.0+ KB
None
Summary Stats:
               age        income  ...  dependents   defaulted
count  200.000000    200.000000  ...  200.000000  200.000000
mean    43.220000  48624.600000  ...    1.510000    0.315000
std     13.271483  15012.343149  ...    1.125269    0.465682
min     21.000000  11534.000000  ...    0.000000    0.000000
25%     31.750000  38592.250000  ...    1.000000    0.000000
50%     44.000000  47118.500000  ...    1.000000    0.000000
75%     55.000000  57924.500000  ...    3.000000    1.000000
max     64.000000  98809.000000  ...    3.000000    1.000000

[8 rows x 7 columns]
Missing Values:
 customer_id        0
age                0
gender             0
income             0
loan_amount        0
loan_term          0
credit_score       0
employment_type    0
marital_status     0
education          0
residence_type     0
dependents         0
purpose            0
defaulted          0
dtype: int64
Duplicate Rows: 0

BarGraph:
![Image](https://github.com/user-attachments/assets/06da31a0-94da-4761-b296-38b535915dd6)
BoxPlot:
![Image](https://github.com/user-attachments/assets/16a34f62-84fa-4142-8d3c-7ab77efac830)
Gender Count:
![Image](https://github.com/user-attachments/assets/f77faba0-cfcd-44d1-9847-38693db11b02)
Deafult Status Count:
![Image](https://github.com/user-attachments/assets/1161c3a2-3135-4cb0-bb0d-3c4d5ca081ac)
Income vs Default :
![Image](https://github.com/user-attachments/assets/ea767957-4798-4788-a2da-46ab0c1e22f5)
Age vs Loan Amount:
![Image](https://github.com/user-attachments/assets/9f9a2fa0-c65e-4654-b3bc-2829529fe444)
Correlation Matrix:
![Image](https://github.com/user-attachments/assets/05c2732b-c72b-4baf-86ac-bfc620a6c04b)
Credit Score Vs Loan Amount:
![Image](https://github.com/user-attachments/assets/af09a552-7b8c-4942-a3dc-13de30218b73)




## 🛠️ Tools & Libraries

- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn (for scaling)

Install dependencies using:
pip install pandas matplotlib seaborn scikit-learn
📊 Sample Visuals
Income Distribution

Default Rate by Gender and Income

Correlation Heatmap of Credit Features

Pair Plots and 3D Scatter Plots

✅ Conclusion
This EDA helps identify:

Key drivers of credit default (e.g., low income, high loan amount)

Data quality issues (missing or skewed data)

The best features to use for predictive modeling

🙋‍♀️ Author
Gadipudi Sirisha (Y21IT029)
Final Year Student — RVR & JC College of Engineering





