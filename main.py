import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("mock_health_data.csv")

df["date"] = pd.to_datetime(df["date"])
df["calories_goal"] = 2000
x = df[df["date"] > "2025-06-15"]
dates = x["date"]
y = x["calories_burned"]
z = x["calories_consumed"]
zy = x["calories_goal"]




plt.plot(dates,y)
plt.plot(dates,z)
plt.plot(dates, zy)


plt.show()



