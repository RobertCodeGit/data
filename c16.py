import csv
import matplotlib.pyplot as plt


filename = 'sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  #get high temperature data
  highs = []
  for row in reader:
    high = int(row[5])
    highs.append(high)


#plot the high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

print(header_row)

for index, column_header in enumerate(header_row):
  print(index, column_header)

print(highs)


#format plot
ax.set_title("Daily high temp 2018", fontsize=24)
