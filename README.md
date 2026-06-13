# 📉 Unemployment Analysis in India

> A data-driven analysis of unemployment trends in India, with a focus on the impact of the COVID-19 pandemic across different regions and time periods.

---

## 📌 Overview

This project analyzes the **unemployment rate in India** before, during, and after the COVID-19 pandemic (2019–2021). Using real-world data, it uncovers region-wise patterns, monthly trends, and the overall economic shock caused by the lockdowns — providing valuable insights through rich visualizations and statistical summaries.

---

## 🎯 Objectives

- Analyze how unemployment rates changed during COVID-19
- Perform region-wise and state-wise breakdown of unemployment
- Visualize trends over time using time-series plots
- Identify the most and least affected states/regions
- Draw meaningful conclusions from statistical analysis

---

## 📊 Dataset

| Feature | Description |
|---------|-------------|
| `Region` | State / region name in India |
| `Date` | Month and year of observation |
| `Frequency` | Data collection frequency (monthly) |
| `Estimated Unemployment Rate (%)` | Unemployment rate (%) |
| `Estimated Employed` | Number of people employed |
| `Estimated Labour Participation Rate (%)` | % of population actively in the workforce |
| `Area` | Urban or Rural classification |

- **Source:** CMIE (Centre for Monitoring Indian Economy)
- **Time Period:** 2019 – 2021

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776ab?style=for-the-badge&logo=python&logoColor=white)

---

## 🔍 Project Workflow

```
1. Data Loading & Inspection
        ↓
2. Data Cleaning & Preprocessing
   - Handling missing values
   - Parsing date columns
   - Renaming & formatting columns
        ↓
3. Exploratory Data Analysis (EDA)
   - Monthly unemployment trend (line chart)
   - Region-wise unemployment (bar chart)
   - Urban vs Rural comparison
   - Correlation heatmap
   - Distribution plots
        ↓
4. COVID-19 Impact Analysis
   - Pre-COVID vs During-COVID comparison
   - Peak unemployment period identification
        ↓
5. Key Insights & Conclusions
```

---

## 📈 Key Findings

| Observation | Detail |
|-------------|--------|
| 📅 Peak Unemployment | April–May 2020 (National Lockdown) |
| 📍 Most Affected Region | Tripura, HR, Bihar recorded highest spikes |
| 🏙️ Urban vs Rural | Urban areas experienced sharper unemployment spikes |
| 📊 Pre-COVID Avg. Rate | ~7–8% |
| 🚨 Peak COVID Rate | ~23–24% (April 2020) |
| 📉 Post-COVID Recovery | Gradual decline from mid-2020 onward |

---

## 💡 Key Insights

- India's unemployment rate **nearly tripled** during the April 2020 lockdown
- **Urban unemployment** was more severely hit than rural, likely due to dependence on non-agricultural sectors
- The economy showed **gradual recovery** from Q3 2020, but some regions took longer to stabilize
- **Labour Participation Rate** also dropped significantly during lockdowns, indicating discouraged workers

---

## 📁 Project Structure

```
UnemploymentAnalysis/
│
├── unemployment_analysis.ipynb    # Main Jupyter Notebook
├── unemployment_rate_india.csv    # Dataset
├── README.md                      # Project documentation
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mayank-Kaneriya1442/UnemploymentAnalysis.git
   cd UnemploymentAnalysis
   ```

2. **Install required libraries**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

3. **Open the notebook**
   ```bash
   jupyter notebook unemployment_analysis.ipynb
   ```

---

## 🌐 Connect with Me

[![Portfolio](https://img.shields.io/badge/Portfolio-4CAF50?style=for-the-badge&logo=netlify&logoColor=white)](https://mayankkaneriya1442.netlify.app/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077b5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mayank-kaneriya-011729363/)
[![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mayank-Kaneriya1442)
[![Email](https://img.shields.io/badge/Email-d14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mayankkaneriya15@gmail.com)

---

⭐ *If you found this project helpful, feel free to star the repository!*
