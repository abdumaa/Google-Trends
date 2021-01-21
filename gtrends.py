# Import manipulation and visualisation packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Import pytrends API
from pytrends.request import TrendReq

# Create a pytrend object. Request data from Google. hl parameter specifies host-language.
pytrends = TrendReq(hl='en-US', tz=360) #, tz=360, retries=10, backoff_factor=0.5

# Daily Trend in Germany
ts_df = pytrends.trending_searches(pn='germany')
ts_df.head()

# Extract data for Covid-related keywords
kw_list = ["lockdown", "vaccine", "unemployment", "zoom"]
pytrends.build_payload(kw_list, cat='0', timeframe='2019-10-01 2021-01-01', geo='US', gprop='')
df_covid = pytrends.interest_over_time()#.drop(['isPartial'], axis = 1)
df_covid.head()

# Interest by region for unemployment
kw_list = ["unemployment"]
pytrends.build_payload(kw_list, cat='0', timeframe='2020-11-01 2020-11-30', geo='US', gprop='')
df_creg = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
df_creg = df_creg.sort_values(by=['unemployment'], ascending=False).reset_index()
df_ur = pd.read_excel('ur_data.xls')
df_ur = df_ur.sort_values(by=['unemployment rate'], ascending=False)
df = pd.merge(df_creg, df_ur, on="geoName")
df['unemployment'].corr(df['unemployment rate'])

# Plot data
plt.figure(figsize=(16, 4))
plt.title('Relative searches of keyword "unemployment" by state in November 2020')
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="geoName", y="unemployment", data=df_creg)
for item in ax.get_xticklabels():
    item.set_rotation(90)
fig = ax.get_figure()
fig.savefig('unemployment.png')

plt.figure(figsize=(16, 4))
plt.title('Unemployment rate by state in November 2020 (U.S. Bureau of Labor Statistics)')
sns.set_theme(style="whitegrid")
ax = sns.barplot(x="geoName", y="unemployment rate", data=df_ur)
for item in ax.get_xticklabels():
    item.set_rotation(90)
fig = ax.get_figure()
fig.savefig('unemployment_rate.png')



# Plot data
df_covid.plot()
plt.ylabel("relative weekly searches")
plt.savefig('covid_searches.png')


# Finding top trending stocks
kw_list2 = ['stock price']
pytrends.build_payload(kw_list2, cat='0', timeframe='now 1-H', geo='', gprop='')
related_df = pytrends.related_queries()
top_queries=[]
rising_queries=[]
for key, value in related_df.items():
    for k1, v1 in value.items():
        if(k1=="top"):
            top_queries.append(v1)
        else:
            rising_queries.append(v1)

top_queries



