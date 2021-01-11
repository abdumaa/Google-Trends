# Import manipulation and visualisation packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import pytrends API
from pytrends.request import TrendReq

# Create a pytrend object. Request data from Google. hl parameter specifies host-language.
pytrends = TrendReq(hl='en-US') #, tz=360, retries=10, backoff_factor=0.5

# Daily Trend in US
trending_searches_df = pytrends.trending_searches(pn='germany')
print(trending_searches_df.head(20))

# Extract data about keyword
kw_list = ["hello"]
pytrends.build_payload(kw_list, cat='0', timeframe='today 2-y', geo='', gprop='') #, timeframe='today 1-y'