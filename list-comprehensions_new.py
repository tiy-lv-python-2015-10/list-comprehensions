import csv

# Remove all vowels from this sentence
text = "List Comprehensions are the Greatest!"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']

for char in text:
    if char in vowels:
        text = text.replace(char, '')
print(text)


# with open("buoy.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# import csv
#
# with open("buoy.csv") as file:
#     reader = csv.DictReader(file)
#     temp_list = [temp["Water Temp"] for temp in reader]
#     print(temp_list)


with open("buoy.csv") as file:
    reader = csv.DictReader(file)
    temp_list = [temp["Water Temp"] for temp in reader]
    x = (', '.join(temp_list))
    print(x)

    # x = float(input(', '.join(temp_list)))


#
# with open("buoy.csv") as file:
#     reader = csv.DictReader(file)
#     temp_list = [temp["Water Temp"] for temp in reader]
#     x = (', '.join(temp_list))
#
#         celsius = float(input(x))
#         fahrenheit = (celsius * 1.8) + 32
#         print(fahrenheit)


#
# def str_to_float(temp_list):
#
#     float_temp_list = [float(temp) for temp in temp_list]
#     return float_temp_list
#
# def string_to_float(list):
#     new_list = [float(items) for items in list]
#     return new_list
