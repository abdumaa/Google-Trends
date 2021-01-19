# Import manipulation and visualisation packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Interest by region
df_creg = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False)
df_creg

# Plot data
df_covid.plot()
plt.ylabel("relative weekly searches")
plt.savefig('covid_searches.png')


# Extract data for e-Commerce-related keywords
kw_list = ["Online auctions", "Online prices"]
pytrends.build_payload(kw_list, cat='0', timeframe='all', geo='US', gprop='')
data_e = pytrends.interest_over_time().drop(['isPartial'], axis = 1)
data_e.head()

# Plot data
data_e.plot()
plt.ylabel("relative weekly searches")
plt.savefig('ecommerce_searches.png')


# Extract data for nba-teams keywords
kw_list = ["Los Angeles Lakers", "Golden State Warriors", "Miami Heat", "Milwaukee Bucks", "Denver Nuggets"]
pytrends.build_payload(kw_list, cat='0', timeframe='2018-01-01 2020-12-31', geo='US', gprop='')
data_nba = pytrends.interest_over_time().drop(['isPartial'], axis = 1)
data_nba.head()

# Plot data
data_nba.plot()
plt.ylabel("relative weekly searches")
plt.savefig('nba_searches.png')



