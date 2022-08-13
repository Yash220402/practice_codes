import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

hour_df = pd.read_csv("hour.csv")

print(hour_df.head())
print(hour_df.dtypes)

# clearing up the attribute names
hour_df.rename(columns={"instant": "rec_id",
						"dteday": "datetime",
						"holiday": "is_holiday",
						"workingday": "is_workingday",
						"weathersit": "weather_condition",
						"hum": "humidity",
						"mnth": "month",
						"cnt": "total_count",
						"hr": "hour",
						"yr": "year"}, inplace=True)

# date time conversion
hour_df["datetime"] = pd.to_datetime(hour_df.datetime)

# categorical variables
hour_df["season"] = hour_df.season.astype("category")
hour_df["is_holiday"] = hour_df.is_holiday.astype("category")
hour_df["weekday"] = hour_df.weekday.astype("category")
hour_df["weather_condition"] = hour_df.weather_condition.astype("category")
hour_df["is_workingday"] = hour_df.is_workingday.astype("category")
hour_df["month"] = hour_df.month.astype("category")
hour_df["year"] = hour_df.year.astype("category")
hour_df["hour"] = hour_df.hour.astype("category")


# Distribution and trends

# season-wise hourly distribution
fig, ax = plt.subplots()
sn.pointplot(data=hour_df[{"hour",
						   "total_count",
						   "season"}],
			 x="hour", y="total_count",
			 hue="season", ax=ax)
ax.set(title="Season wise hourly distribution of counts")
plt.show()

# weekday-wise hourly distribution
fig, ax = plt.subplots()
sn.pointplot(data=hour_df[{"hour",
						   "total_count",
						   "weekday"}],
			 x="hour", y="total_count",
			 hue="weekday", ax=ax)
ax.set(title="Day-wise hourly distribution of counts")
plt.show()

# monthly distribution
fig, ax = plt.subplots()
sn.barplot(data=hour_df[{"month",
						   "total_count"}],
			 x="month", y="total_count")
ax.set(title="Monthly distribution of counts")
plt.show()