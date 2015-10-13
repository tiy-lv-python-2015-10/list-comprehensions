import csv


def remove_vowels(phrase):
    """
    Takes a phrase and returns it with no vowels
    :param phrase: string
    :return: string with vowels removed
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    cons_word = "".join([char for char in phrase if char not in vowels])
    return cons_word


def list_water_temps(csv_file):
    """
    Takes csv file for waves and water and returns a list of water temperatures
    :param csv_file: csv file containing waves and water info
    :return: list of the water temperatures from the file
    """
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        temp_list = [temp["Water Temp"] for temp in reader]
    return temp_list


def str_to_float(temp_list):
    """
    takes a list of temperatures as strings and converts them to floats
    :param temp_list: list of temperatures as strings
    :return: list of temperatures as floats
    """
    float_temp_list = [float(temp) for temp in temp_list]
    return float_temp_list


def cel_to_fahren(temp_list):
    """
    takes a list of temperatures as celsius floats and returns fahrenheit ints
    :param temp_list: list of temperatures as floats in celsius
    :return: list of temperatures as ints in fahrenheit
    """
    fahren_list = [round(temp*9/5+32) for temp in temp_list]
    return fahren_list


def create_waves_dict(csv_file):
    """
    takes a csv file of wave and water info and returns a dictionary with dates and wave height
    :param csv_file: csv file of wave and water info
    :return: dictionary with string Date as the key and float Wave Height as the value
    """
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        waves_dict = {row["Date"]: row["Wave Height"] for row in reader}
        return waves_dict


def avg_hw_one(students_dict):
    """
    takes dictionary of students grades
    :param students_dict: a dict with students as keys and dict of homework grades as values
    :return: float average of homework 1 for all students
    """
    scores = [
        hw['Homework 1']
        for hw in students_dict.values()
        ]
    hw_average = sum(scores) / len(scores)
    return hw_average


student_dict = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                'River': {'Homework 1': 85, 'Homework 2': 91}}


temperature_list = list_water_temps("buoy.csv")
floats_list = str_to_float(temperature_list)
fahrens = cel_to_fahren(floats_list)
wave_dict = create_waves_dict("buoy.csv")
hw_1_average = avg_hw_one(student_dict)

print(temperature_list)
print(floats_list)
print(fahrens)
print(wave_dict)
print(hw_1_average)
