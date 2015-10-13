import csv

def remove_vowel(string):
    vowels =["a", "e", "i", "o", "u"]
    string = "".join([letters for letters in string if letters not in vowels])
    return string

def water_temps(file):
    with open(file) as text:
        reader = csv.DictReader(text)
        water_temp = [row["Water Temp"] for row in reader]
    return water_temp


def string_to_float(list):
    new_list = [float(items) for items in list]
    return new_list


def c_to_f(new_list):
    f_list = [int(float(((9.0/5.0) * items) + 32)) for items in new_list]
    return f_list


def wave_height_dict(file):
    with open(file) as text:
        reader = csv.DictReader(text)
        wave_height = {row["Date"]: row["Wave Height"] for row in reader}
        return wave_height


def average_height(file):
    with open(file) as text:
        reader = csv.DictReader(text)
        average_wave = {row["Date"]: [row["Wave Height"], row["Avg Waves Per Second"]] for row in reader}
        return average_wave


if __name__ == '__main__':
    string = remove_vowel("List Comprehensions are the Greatest!")
    list = water_temps("buoy.csv")
    new_list = string_to_float(list)
    f_list = c_to_f(new_list)
    wave_height = wave_height_dict("buoy.csv")
    average = average_height("buoy.csv")

    print(string)
    print(list)
    print(new_list)
    print(f_list)
    print(wave_height)
    print(average)

