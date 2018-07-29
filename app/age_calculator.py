from _datetime import datetime

now = datetime.now()
current_year = now.year

def ageCalculator(birth_year):

    if isinstance(birth_year, int):
        if birth_year > 0:
            age = current_year - birth_year
            print('You are ' + str(age) + ' years old')
            return age
    return 'Please enter a number.'

