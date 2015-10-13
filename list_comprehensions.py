import csv
import datetime


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


def convert_dates(csv_file):
    """
    creates list of days by number, not sure why
    """
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        date_list = [datetime.datetime.strptime(row["Date"], '%Y-%m-%d').weekday() for row in reader]
    return date_list


def find_average(dict_list, key):
    """
    Takes list of dictionaries containing wave information and returns average of one value
    """
    working_sum = 0
    for num in dict_list:
        working_sum += float(num[key])
    return round(working_sum / len(dict_list), 2)


def find_weekend(csv_file):
    """
    UNFINISHED -- returns one day instead of a weekend
    Fun Factor is calculated by dividing the stat for each dict into the average for each category, and then
    adding the total from all stats together. This method assumes that the larger the stat, the more fun
    """
    weekend_dict_list = []
    with open(csv_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            if datetime.datetime.strptime(row["Date"], '%Y-%m-%d').weekday() == 5 \
                    or datetime.datetime.strptime(row["Date"], '%Y-%m-%d').weekday() == 6:
                weekend_dict_list.append(row)

    wave_period_avg = find_average(weekend_dict_list, 'Wave Period')
    water_temp_avg = find_average(weekend_dict_list, 'Water Temp')
    wave_height_avg = find_average(weekend_dict_list, 'Wave Height')
    waves_per_sec_avg = find_average(weekend_dict_list, 'Avg Waves Per Second')

    for weekend_dict in weekend_dict_list:
        fun_factor = (float(weekend_dict['Water Temp']) / water_temp_avg) + \
                     (float(weekend_dict['Wave Period']) / wave_period_avg) + \
                     (float(weekend_dict['Avg Waves Per Second']) / waves_per_sec_avg) + \
                     (float(weekend_dict['Wave Height']) / wave_height_avg)
        weekend_dict['Fun Factor'] = round(fun_factor, 2)

    weekend_fun_list = {datetime.datetime.strptime(weekend_dict['Date'], '%Y-%m-%d'): weekend_dict['Fun Factor']
                        for weekend_dict in weekend_dict_list}

    cur_fun_score = 0
    fun_date = datetime.date
    for date, fun_score in weekend_fun_list.items():
        if fun_score > cur_fun_score:
            cur_fun_score = fun_score
            fun_date = date

    return fun_date


if __name__ == '__main__':
    best_day = find_weekend("buoy.csv")
    print("The best day to go is {}".format(best_day))

"""
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
"""