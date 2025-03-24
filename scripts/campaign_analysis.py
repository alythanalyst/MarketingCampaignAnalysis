import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

pd.set_option('display.width', None)
df = pd.read_csv('Campaign_Data.csv')
df['CTR'] = df['Clicks'] / df['Impressions'] * 100
df['Conversion_Rate'] = df['Conversions'] / df['Clicks'] * 100
df['Cost_per_Click'] = df['Total_Spend'] / df['Clicks']
df['Cost_per_Conversion'] = df['Total_Spend'] / df['Conversions']
df['ROAS'] = df['Revenue_Generated'] / df['Total_Spend']


df.to_csv('Campaign_Data_with_metrics.csv', index=False)
