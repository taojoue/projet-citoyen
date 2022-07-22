import pandas as pd
import matplotlib.pyplot as plt

df2020 = pd.read_csv("./Data/radiees2020.csv", sep=';', header=0, encoding='utf-8', dtype={'code_postal': 'str'})

df2020['date_radiation'] = pd.to_datetime(df2020['date_radiation'], errors='coerce', infer_datetime_format=True)
closureBusiness2020 = df2020.set_index('date_radiation').resample('M')['siren'].count()

df2021 = pd.read_csv("./Data/radiees2021.csv", sep=';', header=0, encoding='utf-8', dtype={'code_postal': 'str'})

df2021['date_radiation'] = pd.to_datetime(df2021['date_radiation'], errors='coerce', infer_datetime_format=True)
closureBusiness2021 = df2021.set_index('date_radiation').resample('M')['siren'].count()

df2022 = pd.read_csv("./Data/radiees2022.csv", sep=';', header=0, encoding='utf-8', dtype={'code_postal': 'str'})

df2022['date_radiation'] = pd.to_datetime(df2022['date_radiation'], errors='coerce', infer_datetime_format=True)
closureBusiness2022 = df2022.set_index('date_radiation').resample('M')['siren'].count()

df = pd.concat([closureBusiness2020, closureBusiness2021, closureBusiness2022])

print(df)


# df["date_radiation"] = df["date_radiation"].astype("datetime64")
# df.set_index('date_radiation').resample('M')["siren"].count().plot(kind="line")


plt.show()
plt.close()
