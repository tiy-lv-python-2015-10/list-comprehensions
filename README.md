# List Comprehensions

## Description

Implement various List and Dictionary Comprehensions from a CSV file

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* List Comprehensions
* Dictionary Comprehensions
* Nested Comprehensions

### Performance Objectives

After completing this assignment, you should be able to:

* Open and read CSV files
* Create a List Comprehension
* Create a Dictionary Comprehension
* Convert a string type to a datetime type

## Details

### Deliverables

* A GitHub repo called list-comprehensions containing at least:
  * `README.md` file explaining how to run your project
  * a module called `list_comprehensions`
  * tests for `list_comprehensions`

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

Implement these List and Dictionary Comprehensions, each as a function:

  * Remove all vowels from this sentence `List Comprehensions are the Greatest!`
  * Create a list of Water Temps for each day from `buoy.csv`
  * Convert the Water Temps from a string to a float
  * Convert the Water Temps from Celsius to Fahrenheit rounded to an int
  * Create a dictionary with Date as the key and Wave Height as the value
  * Create a dictionary with the average wave height for each day
  * Using the following dictionary:
  `{'Gale': {'Homework 1': 88, 'Homework 2': 76},
 'Jordan': {'Homework 1': 92, 'Homework 2': 87},
 'Peyton': {'Homework 1': 84, 'Homework 2': 77},
 'River': {'Homework 1': 85, 'Homework 2': 91}}`
    Create a nested comprehension to get the average of the Homework 1 grades.

## Hard Mode

In addition to the requirements from **Normal Mode**:

  * Convert each Date in normal mode (bouy.csv) to its numerical day of the week,
    then create a list of values for each day of the week
  * Write a function that can take a dictionary of bouy data and return the best weekend to take a trip. Include the criteria
  as to how it chooses the best weekend.
 

## Notes

In order to change the Date to its numerical day of the week, you will need
to use `defaultdict` with the `datetime` and `calendar` modules. This will need
to be done as a function, not a Comprehension

## Additional Resources

* [List Comprehension documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [How to Use List Comprehensions by Example](http://howchoo.com/g/ngi2zddjzdf/how-to-use-list-comprehension-in-python)
