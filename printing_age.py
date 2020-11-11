# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def print_age(age_int):
    print('Age:', age_int)


def get_curr_year():
    cur_year = 2020
    return cur_year


def calculate_age(birth_yr_int):
    cur_yr = get_curr_year()
    age = cur_yr - birth_yr_int
    return age


def make_int(a_str):
    the_float = float(a_str)
    the_int = int(the_float)
    return the_int


def get_birth_year():
    birth_yr_str = input('What is your birth-year? ')
    birth_yr_int = make_int(birth_yr_str)
    return birth_yr_int


def printing_age():
    # print age
    birth_year = get_birth_year()
    age = calculate_age(birth_year)
    print_age(age)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # invoke the modules' main function
    printing_age()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
