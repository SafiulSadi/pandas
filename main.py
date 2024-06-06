import pandas

data = pandas.read_csv("./weather-data.csv")

# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)sdflkjasldj
temp_list = data["temp"].to_list()
print(temp_list)
# learned the basics of working with pandas
print(temp_list)
# 