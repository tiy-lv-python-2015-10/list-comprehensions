from list_comprehensions import *

student_dict = {'Gale': {'Homework 1': 75, 'Homework 2': 76},
                'Jordan': {'Homework 1': 60, 'Homework 2': 87},
                'Peyton': {'Homework 1': 65, 'Homework 2': 77},
                'River': {'Homework 1': 40, 'Homework 2': 91}}


def test_remove_vowels():
    assert remove_vowels("English Motherfucker do you speak it! Say what again.") == \
                            "nglsh Mthrfckr d y spk t! Sy wht gn."


def test_list_water_temps():
    # bad test: I should create similar csv file and run a test on that?
    assert list_water_temps("buoy.csv") == ['26.5', '26.2', '26.2', '26.2', '26.5',
                                            '26.9', '27.0', '26.9', '27.1', '27.0',
                                            '26.9', '26.8', '26.9', '27.1', '27.1',
                                            '27.2', '27.5', '27.7', '27.6', '28.1',
                                            '27.5', '27.7', '27.4', '27.4', '28.0',
                                            '28.7', '28.9', '28.5', '28.1', '27.8']


def test_str_to_float():
    assert str_to_float(['26.5', '26.2', '27.7']) == [26.5, 26.2, 27.7]


def test_cel_to_fahren():
    assert cel_to_fahren([26.5, 26.2, 27.7]) == [80, 79, 82]


def test_create_waves_dict():
    # bad test: same for this one
    assert create_waves_dict("buoy.csv") == {'2015-08-04': '1.62', '2015-08-06': '4.09', '2015-08-22': '1.71',
                                             '2015-08-27': '0.64', '2015-08-26': '0.8', '2015-08-08': '2.18',
                                             '2015-08-18': '1.51', '2015-08-14': '1.8', '2015-08-19': '1.54',
                                             '2015-08-23': '2.02', '2015-08-07': '3.52', '2015-08-25': '0.98',
                                             '2015-08-13': '1.81', '2015-08-28': '0.89', '2015-08-03': '1.89',
                                             '2015-08-01': '1.55', '2015-08-15': '1.75', '2015-08-10': '2.2',
                                             '2015-08-09': '2.14', '2015-08-31': '1.83', '2015-08-17': '1.43',
                                             '2015-08-30': '1.7', '2015-08-11': '1.8', '2015-08-20': '1.52',
                                             '2015-08-05': '1.72', '2015-08-29': '1.42', '2015-08-12': '1.99',
                                             '2015-08-21': '1.47', '2015-08-16': '1.6', '2015-08-02': '1.97'}


def test_avg_hw_one():
    assert avg_hw_one(student_dict) == 60.0

