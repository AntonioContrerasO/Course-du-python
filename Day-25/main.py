# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#     clean_data = []
# #     for i in data:
# #         clean_data.append(i.strip())
#
# # import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             print(row)
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
import pandas
#
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

# _list = data["temp"].to_list()
# average = data["temp"].mean()
# max_of_the_list = data["temp"].max()
# print(max_of_the_list)
#
# print(data.condition)
#
# print(data[data.day == "Monday"])

# print(data[data.temp == max_of_the_list])

monday = data[data.day == "Monday"]
monday['temp'] = int(monday.temp) * 1.8 + 32
print(monday.temp)

# data_dict = {"students":["Amy","James","Angela"],"scores":[76,56,65]}
#
# data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")
#
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# count_black = len(data[data["Primary Fur Color"] == "Black"])
# print(data["Primary Fur Color"])
# count_gray = len(data[data["Primary Fur Color"] == "Gray"])
# count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# data_dict = {"Color": ["grey", "red", "black"], "Count": [count_gray, count_cinnamon, count_black]}
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("squirrel_count.csv")
