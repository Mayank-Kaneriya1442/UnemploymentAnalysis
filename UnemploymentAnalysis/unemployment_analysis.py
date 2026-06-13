import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

def main():
    print("Loading and processing unemployment data...")
    df = pd.read_csv('dataset/Unemployment in India.csv')
    df.columns = df.columns.str.strip()

    # Data cleaning
    df['Date'] = pd.to_datetime(df['Date'].str.strip(), dayfirst=True)
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Month_Name'] = df['Date'].dt.strftime('%b')

    df.dropna(subset=['Estimated Unemployment Rate (%)'], inplace=True)
    
    df.rename(columns={
        'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
        'Estimated Employed': 'Employed',
        'Estimated Labour Participation Rate (%)': 'Labour_Participation'
    }, inplace=True)

    # Flag COVID period
    df['Period'] = np.select(
        [df['Year'] == 2019, df['Year'].isin([2020, 2021])],
        ['Pre-COVID (2019)', 'COVID (2020-2021)'],
        default='Post-COVID (2022)'
    )

    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    print("Generating plots...")
    
    # 1. National trend
    national = df.groupby('Date')['Unemployment_Rate'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(national['Date'], national['Unemployment_Rate'], color='#185FA5', lw=2)
    ax.fill_between(national['Date'], national['Unemployment_Rate'], alpha=0.1, color='#185FA5')
    
    ax.axvspan(pd.Timestamp('2020-03-01'), pd.Timestamp('2021-12-01'), 
               alpha=0.1, color='red', label='COVID-19 Period')
    
    ax.set_title('Unemployment Rate Trend (India)')
    ax.set_ylabel('Unemployment Rate (%)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45)
    ax.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_national_trend.png'))
    plt.close()

    # 2. Top 10 States
    state_avg = df.groupby('Region')['Unemployment_Rate'].mean().nlargest(10)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=state_avg.values, y=state_avg.index, color='#185FA5', ax=ax)
    ax.set_title('Top 10 States by Avg Unemployment Rate')
    ax.set_xlabel('Unemployment Rate (%)')
    ax.set_ylabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_top_states.png'))
    plt.close()

    # 3. COVID Impact
    covid_avg = df.groupby('Period')['Unemployment_Rate'].mean().reindex([
        'Pre-COVID (2019)', 'COVID (2020-2021)', 'Post-COVID (2022)'
    ]).dropna()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    covid_avg.plot(kind='bar', color=['#4CAF50', '#E24B4A', '#185FA5'], ax=ax)
    ax.set_title('Unemployment: Pre-COVID vs COVID vs Post-COVID')
    plt.xticks(rotation=0)
    ax.set_ylabel('Avg Rate (%)')
    ax.set_xlabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_covid_impact.png'))
    plt.close()

    # 4. Monthly Heatmap
    pivot = df.pivot_table(index='Year', columns='Month_Name', values='Unemployment_Rate', aggfunc='mean')
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    pivot = pivot.reindex(columns=[m for m in months if m in pivot.columns])
    
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.heatmap(pivot, annot=True, fmt='.1f', cmap='RdYlGn_r', ax=ax)
    ax.set_title('Monthly Unemployment Rate Heatmap')
    ax.set_xlabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_heatmap.png'))
    plt.close()

    # 5. Region-wise Boxplot
    top_regions = df.groupby('Region')['Unemployment_Rate'].mean().nlargest(8).index
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df[df['Region'].isin(top_regions)], x='Region', y='Unemployment_Rate', ax=ax)
    ax.set_title('Unemployment Rate Distribution - Top 8 States')
    plt.xticks(rotation=30, ha='right')
    ax.set_xlabel('')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_region_boxplot.png'))
    plt.close()

    # 6. Correlation Heatmap
    cols = ['Unemployment_Rate', 'Labour_Participation', 'Month', 'Year']
    cols = [c for c in cols if c in df.columns]
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df[cols].corr(), annot=True, fmt='.2f', cmap='coolwarm', ax=ax)
    ax.set_title('Feature Correlation')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'unemployment_correlation.png'))
    plt.close()

    # Key Insights summary
    pre_avg = df.loc[df['Year'] == 2019, 'Unemployment_Rate'].mean()
    covid_avg_val = df.loc[df['Year'] == 2020, 'Unemployment_Rate'].mean()
    
    print("\n--- Key Insights ---")
    if pd.notna(pre_avg):
        print(f"Pre-COVID avg rate (2019): {pre_avg:.2f}%")
    if pd.notna(covid_avg_val):
        print(f"COVID peak avg rate (2020): {covid_avg_val:.2f}%")
    if pd.notna(pre_avg) and pd.notna(covid_avg_val):
        print(f"Increase due to COVID: +{covid_avg_val - pre_avg:.2f} percentage points")
        
if __name__ == "__main__":
    main()