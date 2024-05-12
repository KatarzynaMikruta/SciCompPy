import numpy as np
import pandas as pd
import datetime as dt

current_date = dt.datetime.now()
first_day = dt.datetime(current_date.year, current_date.month, 1)
date_range = [first_day + dt.timedelta(days=i) for i in range(current_date.day)]

temperature_data = np.random.randint(10, 30, len(date_range))

temperature_series = pd.Series(temperature_data, index=date_range)

print(temperature_series)