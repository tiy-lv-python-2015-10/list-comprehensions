import csv


def remove_vowels(a_text):
    vowels = ["o", "i", "a", "e", "u"]
    no_vowels = []
    [no_vowels.append(letter)for letter in a_text if letter not in vowels]
    answer1 = ''.join(no_vowels)
    return answer1


def water_temp(a_file):
    with open(a_file) as raw:
        read_it = csv.DictReader(raw)
        water_temps = [row["Water Temp"] for row in read_it]
        return water_temps


def make_float(a_list):
    list2 = [float(stuff)for stuff in a_list]
    return list2


def convert_f(list_c):
    list_f = [int(float(1.8 * a_temp) + 32) for a_temp in list_c]
    return list_f


def date_wave_height(a_file):
    with open(a_file) as raw:
        read_it = csv.DictReader(raw)
        w_height = {row["Date"]: row["Wave Height"] for row in read_it}
        return w_height


def ave_wave_height(a_file):
    with open(a_file) as raw:
        read_it = csv.DictReader(raw)
        ave_height = {row["Date"]: [row["Wave Height"], row["Avg Waves Per Second"]]for row in read_it}
        return ave_height


"""take report and for every value for homework 1 put in a list then take that
list and add it together and get the average """


def ave_scores(report):
    scores = [
        grades["Homework 1"]for grades in report.values()
            ]
    ave = sum(scores) / len(scores)
    return ave


if __name__ == '__main__':
    report = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
              'Jordan': {'Homework 1': 92, 'Homework 2': 87},
              'Peyton': {'Homework 1': 84, 'Homework 2': 77},
              'River': {'Homework 1': 85, 'Homework 2': 91}}
    a_text = remove_vowels("list Comprehensions are the Greatest")
    a_file = water_temp("buoy.csv")
    a_list = make_float(a_file)
    list_f = convert_f(a_list)
    date_height = date_wave_height("buoy.csv")
    ave_height = ave_wave_height("buoy.csv")
    ave = ave_scores(report)
    print("1", a_text)
    print("2", a_file)
    print("3", a_list)
    print("4", list_f)
    print("5", date_height)
    print("6", ave_height)
    print("7", ave)
