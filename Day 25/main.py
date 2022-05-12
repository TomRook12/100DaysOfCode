#with open("weather_data.csv", mode="r") as file:
#    weather = file.readlines()
#
#print(weather)

#import csv
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#
#
#print(temperatures)
#
#import pandas
#
#data = pandas.read_csv("weather_data.csv")
#
#max = data["temp"].max()
##print(data.condition)
#monday = data[data.day == "Monday"]
#monday_celcius = int(monday.temp)
#monday_fahrenheit = monday_celcius*(9/5) + 32
#print(monday_fahrenheit)
#
#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 75, 60]
#}
#
#data = pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

#TODO: Fur colour problem, count the nbumbers of each fur type
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())
