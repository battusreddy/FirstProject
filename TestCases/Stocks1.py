import pandas as pd
import numpy as np
import iexfinance
from iexfinance.stocks import get_historical_data
from datetime import datetime, date

# start date should be within 5 years of current date according to iex API we have used
# The more data we have, the better results we get!

start = datetime(2020, 1, 1)
end = date.today()
# use your token in place of token which you will get after signing up on IEX cloud
# Head over to https://iexcloud.io/ and sign-up to get your API token
df = get_historical_data("IDEA", start=start, end=end, output_format="pandas", token="pk_340de0f365ab4527857d07974123a3fa")
print (df)