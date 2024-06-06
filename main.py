import pandas

data = pandas.read_csv("./weather-data.csv")

# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)sdflkjasldj
# temp_list = data["temp"].to_list()
# print(temp_list)
# # learned the basics of working with pandas
# print(temp_list)
# # 
# print(data["temp"].max())  
# print(data["condition"])
# print(data.condition)

# get data in Row
# print(data[data.day == "Monday"]) 
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition )
# monday_temp = monday.temp
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# create a dataframe from scratch
data_dict= {
  "students": ["Amy", "James", "Angela"],
  "scores": [76, 56, 65]
}
data1 = pandas.DataFrame(data_dict)
print(data1)

data1.to_csv("newData.csv")







