# Import manipulation and visualisation packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import pytrends API
from pytrends.request import TrendReq

# Create a pytrend object. Request data from Google. hl parameter specifies host-language.
pytrends = TrendReq(hl='en-US', tz=360) #, tz=360, retries=10, backoff_factor=0.5

# Daily Trend in US
trending_searches_df = pytrends.trending_searches(pn='germany')
print(trending_searches_df.head(20))

# Extract data about keyword
kw_list = ["lockdown", "vaccine", "homeschooling", "mortality"]
pytrends.build_payload(kw_list, cat='0', timeframe='2019-01-01 2021-01-01', geo='US', gprop='')
data = pytrends.interest_over_time().drop(['isPartial'], axis = 1)
data.head()

# Plot data

data.plot()
plt.ylabel("relative weekly searches")
plt.savefig('covid_searches.png')

#sns.lineplot(data=data, x="date", y="depression")
