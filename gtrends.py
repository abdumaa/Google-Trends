# Import manipulation and visualisation packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import pytrends API
from pytrends.request import TrendReq

# Create a pytrend object. Request data from Google. hl parameter specifies host-language.
pytrends = TrendReq(hl='en-US') #, tz=360, retries=10, backoff_factor=0.5

# Extract data about keyword
kw_list = ["anosmia"]
pytrends.build_payload(kw_list, timeframe='today 1-y')
