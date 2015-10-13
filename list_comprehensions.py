import csv
import datetime

vowels = ["a", "e", "i", "o", "u"]
string = "List Comprehensions are the Greatest!"


def remove_vowels(string):
    no_vowels = []
    [no_vowels.append(string[i]) for i in range(0, len(string)) if string[i] not in vowels]
    no_vowels = "".join(no_vowels)
    return no_vowels


def daily_water_temps(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file)  # reader is an iterable
        water_temps = []
        for row in reader:  # loop through every row
            water_temps.append(row[4])
    return (water_temps[1:-1])


def string_to_float(string):
    floats = []
    for i in range(0, len(string)):
        floats.append(float(string[i]))
    return floats


def celsius_to_fahrenheit(celsius):
    # (°C × 9/5) + 32 = °F
    fahrenheit = []
    for i in range(0, len(celsius)):
        fahrenheit.append(int((((celsius[i] * (9 / 5)) + 32))))
    return fahrenheit


def date_wave_height(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file) #reader is an iterable
        wave_heights = []
        dates = []
        for row in reader: #loop through every row
            dates.append(row[5])
            wave_heights.append(row[1])
        wave_height_dict = dict(zip(dates,wave_heights))
        wave_height_dict.pop("Date", None)
    return wave_height_dict




def average_wave_height_per_day(csv_file):
    with open(csv_file) as file:
        reader = csv.reader(file) #reader is an iterable
        wave_heights = []
        dates = [ "saturday","sunday","monday", "tuesday", "wednesday", "thursday", "friday"]
        for row in reader: #loop through every row
            dates.append(row[5])
            wave_heights.append(row[1])
        #wave_height_dict = dict(zip(dates,wave_heights))
        #wave_height_dict.pop("Date", None)
        wave_heights.pop(0)
        first_seven = wave_heights[:7]
        second_seven = wave_heights[7:14]
        q = [x + y for x, y in zip(first_seven, second_seven)]
        third_seven = wave_heights[14:21]
        fourth_seven = wave_heights[21:28]
        last_two = wave_heights[28:30]
        print(first_seven)
        print(second_seven)
        print(third_seven)
        print(fourth_seven)
        print(last_two)
        print(q)
        #[x + y for x, y in zip(first, second)]
    return wave_heights


if __name__ == '__main__':
    # print(remove_vowels(string))
    # print(daily_water_temps("buoy.csv"))
    # print(string_to_float(daily_water_temps("buoy.csv")))
    # print(celsius_to_fahrenheit(string_to_float(daily_water_temps("buoy.csv"))))

    #print(date_wave_height("buoy.csv"))
    print(average_wave_height_per_day("buoy.csv"))
    # x = [2, 4, 7, 12, 3]
    # sum_of_all_numbers= sum(x)
    # print(sum_of_all_numbers)
