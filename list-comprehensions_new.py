import csv

# Remove all vowels from this sentence
text = "List Comprehensions are the Greatest!"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U']

for char in text:
    if char in vowels:
        text = text.replace(char, '')
print(text)


# water Temp for each day from buoy.csv
with open("buoy.csv") as file:
    reader = csv.DictReader(file)
    temp_list = [temp["Water Temp"] for temp in reader]
    x = (', '.join(temp_list))
    print(x)


# convert string to float
float_temp = [float(temp) for temp in temp_list]
print(float_temp)

# celsius to fahrenheit rounded to an int
with open("buoy.csv") as file:
    fahrenheit = []
    for temp in file:
        fahrenheit.append(round(temp * (9 / 5)) + 32)
    print(fahrenheit)

# create dic with date as the key wave height as value
with open("buoy.csv") as file:
    reader = csv.DictReader(file)
    dictionary = {row["Date"] and row["Wave Height"] for row in reader}
    print(dictionary)

# create dic with average wave height for each day
with open("buoy.csv") as file:
    reader = csv.DictReader(file)
    wave_height = [height["Wave Height"] for height in reader]
    x = (', '.join(wave_height))
    days_total = "31"
    average_wave_height = (int(input(x) / int(input(days_total))))
    print(average_wave_height)


# use following dictionary and
# create nested comprehension to get an average of homework 1

dictionary = {
    'Gale': {'Homework 1': 88, 'Homework 2': 76},
    'Jordan': {'Homework 1': 92, 'Homework 2': 87},
    'Peyton': {'Homework 1': 84, 'Homework 2': 77},
    'River': {'Homework 1': 85, 'Homework 2': 91}
}


