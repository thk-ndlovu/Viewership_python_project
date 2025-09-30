# Viewership Trend Over Time
time_trend = df.groupby("DateID")["TotalTimeWatched"].sum()

time_trend.plot(kind="line")
plt.title("Viewership Trend Over Time")
plt.ylabel("Total Time Watched")
plt.xlabel("Date")
plt.show()
