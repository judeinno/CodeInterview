from _datetime import datetime

now = datetime.now()
current_year = now.year

"""This function caculates the age of a person"""
def ageCalculator(birth_year):

    if isinstance(birth_year, int):
        if birth_year > 0:
            age = current_year - birth_year
            print('You are ' + str(age) + ' years old')
            return age
    else:
        print('Please enter a number.')
        return 'Please enter a number.'

