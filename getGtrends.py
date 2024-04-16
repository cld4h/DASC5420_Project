#!pip install pytrends

from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=240, timeout=(10,25))
# tz, timezone should be EDT

kw_list = ['Apple Watch', 'MacBook', 'AirPods', 'iPad', 'iPhone']

# half-year interval gives the daily trends
tf_list = ['2016-04-01 2016-09-30' ,'2016-10-01 2017-03-31' ,'2017-04-01 2017-09-30' ,'2017-10-01 2018-03-31' ,'2018-04-01 2018-09-30' ,'2018-10-01 2019-03-31' ,'2019-04-01 2019-09-30' ,'2019-10-01 2020-03-31' ,'2020-04-01 2020-09-30' ,'2020-10-01 2021-03-31' ,'2021-04-01 2021-09-30' ,'2021-10-01 2022-03-31' ,'2022-04-01 2022-09-30' ,'2022-10-01 2023-03-31' ,'2023-04-01 2023-09-30' ,'2023-10-01 2024-03-31']

trends_list = list()
for t in tf_list:
  pytrends.build_payload(kw_list, timeframe=t)
  trends_list.append(pytrends.interest_over_time())

combined_df = pd.concat(trends_list, axis=0)
combined_df.to_csv("Gtrends.csv")
