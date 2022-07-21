import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Data/radiees2020.csv", sep=';', header=0, encoding='utf-8', dtype={'code_postal': 'str'})

df['date_radiation'] = pd.to_datetime(df['date_radiation'], errors='coerce', infer_datetime_format=True)
closureBusiness = df.set_index('date_radiation').resample('M')['siren'].count()

print(closureBusiness)

df["date_radiation"] = df["date_radiation"].astype("datetime64")
df.set_index('date_radiation').resample('M')["siren"].count().plot(kind="line")


plt.show()
plt.close()
