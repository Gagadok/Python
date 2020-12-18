# Data generation

from dateutil.relativedelta import relativedelta
import datetime
import random
from datetime import timedelta
import string

class Data:
    
    # Function for calculating a random date for the last 5 years
    def random_date(self, number_of_years):
        now = datetime.datetime.now()
        years_ago = now - relativedelta(years = number_of_years)
        delta = now - years_ago
        return now - timedelta(random.randint(0, delta.days))
    
    # Random Latin characters
    def random_Latin_characters(self, num):
        Latin_characters = ""
        for i in range(num):
            # The ascii table is used
            Latin_characters = Latin_characters + random.choice(string.ascii_letters)
        return Latin_characters
    
    # Random Russian characters
    def random_Russian_characters(self, num):
        a = ord('а')
        # The list of Russian characters is formed by the character code
        Russian_letter = ''.join([chr(i) for i in range(a, a + 6)] +
                                 [chr(a + 33)] +
                                 [chr(i) for i in range(a + 6, a + 32)])
        capital_а = ord('А')
        Russian_letter = Russian_letter + ''.join([chr(i) for i in range(capital_а, capital_а + 6)]
                                                  + [chr(ord('Ё'))] +
                                                  [chr(i) for i in range(capital_а + 6, capital_а + 32)])
        Russian_characters = ""
        for i in range(num):
            Russian_characters = Russian_characters + random.choice(Russian_letter)
        return Russian_characters
    
    # Random even integers
    def random_even_number(self, start, end):
        number = random.randint(start, end)
        # While the lowest byte of the number == 1-generate a new random integer
        while number & 1:
            number = random.randint(start, end)
        return number
    
    # Random real number with 8 decimal places
    def random_real_number(self, start, end, number_of_decimal_places):
        return round(random.uniform(start, end), number_of_decimal_places)
    
#-----------------------------------------------

_inst = Data()
random_date = _inst.random_date
random_Latin_characters = _inst.random_Latin_characters
random_Russian_characters = _inst.random_Russian_characters
random_even_number = _inst.random_even_number
random_real_number = _inst.random_real_number