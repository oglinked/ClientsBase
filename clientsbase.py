""" WollPay Clients Base (Version 00.05 of clientsbase.py). """

import datetime
import pytz
import csv
import os
from pathlib import Path
import re

message_cyrillic = 'No cyrillic letters are allowed in this field!'
message_latin = 'Only Latin letters are allowed in this field!'

def cyrillic_presence_test(str_to_valid, message = message_latin):
    """No cyrillic letters please."""
    result = re.findall("[а-яА-Я]", str_to_valid)
    if not bool(result):
        pass
    else:
        print(f'Error: {message}')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid, message)
        # It was Recursion.
    return str_to_valid


def remove_tabs(string):
    """Code to remove tabulation."""
    if '\t' in string:
        print('Warning: Inputed Tabs characters was removed!')
    return string.replace('\t', '')


def remove_whitespaces(string):
    """Code to remove whitespaces"""
    if ' ' in string:
        print('Warning: Inputed whitespaces was removed!')
    return string.replace(" ", "")


def remove_tabs_and_whitespaces(string):
    """Code to remove tabulation and whitespaces."""
    string = remove_tabs(string)
    string = remove_whitespaces(string)
    return string


def remove_cyrillic_and_tabs(string, message=message_latin):
    string = cyrillic_presence_test(string, message)
    string = remove_tabs(string)
    return string


def cid_validation(cid):
    """Validation of CID."""
    cid = cyrillic_presence_test(cid, message_cyrillic)
    cid = remove_tabs_and_whitespaces(cid)
    if len(cid) < 1: # Minimum 1 character should be present.
        print('Error: To few characters inputed.')
        cid = input('Repeat Input: ')
        cid = cid_validation(cid) # Recursion.
    cid = valid_isalnum(cid) # To test the presence of
    # Latin alphabet and decimal digits only. 
    return cid


def valid_isalnum(str_to_valid):
    """Validation the latin alphabet and decimal digits
    presence only. It's for field CID only.
    Return latters on the upper case.
    """
    if str_to_valid.isalnum():
        pass
    else:
        print('Error: Only latin latters and decimal digits \
are allowed in this field.')
        str_to_valid = input('Repeat Input: ')
        str_to_valid = cid_validation(str_to_valid) # Go to CID validation.
    return str_to_valid.upper()


def str_valid_to_upper(str_to_valid):
    """ String validation.
    Capital letters only. No numbers.
    str_to_valid  parametr (Input string to validation).
    """
    str_to_valid = cyrillic_presence_test(str_to_valid)
    str_to_valid = remove_tabs(str_to_valid)
    if str_to_valid.isalpha():
        pass
    else:
        print('Error: Only latin letters are allowed in this field!')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = cyrillic_presence_test(str_to_valid)
        str_to_valid = remove_tabs(str_to_valid)
        str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.
    str_to_valid = str_to_valid.upper()
    return str_to_valid  


def force_empty_phone_number(phone_number):
    """Empty phone_number"""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs_and_whitespaces(result)
    if result == 'y' or result == 'Y':
        phone_number = ''
    else:
        phone_number = phone_number_validation(phone_number) # Validation.
    return phone_number


def empty_phone_number(phone_number):
    """Test phone_number input."""
    phone_number = cyrillic_presence_test(phone_number, message_cyrillic)
    phone_number = remove_tabs_and_whitespaces(phone_number) 
    if phone_number == '':
        phone_number = force_empty_phone_number(phone_number)
    else:
        phone_number = phone_number_validation(phone_number) # Validation.
    return phone_number


def phone_number_validation(number):
    """Phone number validation.
    Sign '+' allowed on the first position.
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    # Empty phone number is not allowed.
    if number != '': 
        pass                               
    else:
        print('Error: more digits should be in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '': return number
    # Here 6 is minimum digits in phone number.
    if len(number) >= 6: 
        pass                               
    else:
        print('Error: more digits should be in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '': return number
    first_sign = ['+','0','1','2','3','4','5','6','7','8','9']
    if number[0] in first_sign:
        pass
    else:
        print('Error: Only decimal digits and "+" sign \
on first position are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number) 
        if number == '': return number
    sub_number = number[1:] # Validation the string after first sign.
    if sub_number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits and "+" sign \
on first position are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = empty_phone_number(number)
        if number == '': return number 
    return number


def one_or_zero(string_to_valid):
    """Only "1" or "0" are valid values to input parameter."""
    string_to_valid = cyrillic_presence_test(string_to_valid,
                                             message_cyrillic)
    string_to_valid = remove_tabs_and_whitespaces(string_to_valid)
    if string_to_valid == "1" or string_to_valid == "0":
        pass
    else:
        print('Error: Only "1" or "0" without spaces \
are allowed in this field!')
        string_to_valid = input('Please repeat input: ')
        string_to_valid = cyrillic_presence_test(string_to_valid,
                                             message_cyrillic)
        string_to_valid = remove_tabs_and_whitespaces(string_to_valid)
        string_to_valid = one_or_zero(string_to_valid) # Recursion.
    return string_to_valid

    
def valid_decimal(number):
    """ Number validation.
    Decimal digits are allowed only.
    number - parametr (Input string to validation).
    """
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    if number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits are allowed in this field!')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = valid_decimal(number) # Recursion.
    return number    


def check_letters(str_to_valid):
    """Checking for absence of letters in given string."""
    str_to_valid = cyrillic_presence_test(str_to_valid)
    str_to_valid = remove_tabs(str_to_valid)
    result = True # Initializing result variable.
    for i in str_to_valid:
        if i.isalpha(): # if string has letter:
            result = False
    return result


def empty_date(date):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave the field empty y/n?.
    """
    date = cyrillic_presence_test(date, message_cyrillic)
    date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
    if date == '':
        date = force_empty_date(date)
    else:
        date = date_validation(date)
    return date


def force_empty_date(date):
    """Empty (or current) date."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs(result)
    if result in ['y', 'Y']:
        # date = '' # Empty field.
        date = datetime.datetime.now(pytz.timezone('Poland')) \
                .strftime("%m/%d/%Y") # Getting current date.
    else:
        date = date_validation(date) # Go to date_validation().
    return date


def date_validation(date):
    """ Date validation.
    date - parameter (Inputed date to validation).
    """
    date = cyrillic_presence_test(date, message_cyrillic)
    date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
    # Testing the length of the field.
    if len(date) == 10:
        pass
    else:
        print('Error: In this field should be 10 characters.')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    # Testing the absence of alphabetical letters.
    if check_letters(date):
        pass
    else:
        print('Error: No letters are allowed in this field!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    #Testing the presence of two "/" characters.
    if date[2] == date[5] == '/':
        pass
    else:
        print('Error: Check the presence of "/" characters in right places!')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    # Testing "mm" in mm/dd/yyyy
    mm = ['01','02','03','04','05','06','07','08','09','10','11','12']
    month = date[0] + date[1]
    if month in mm:
        pass
    else:
        print('Error: The Month value should be [01,...,12].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    # Testing "dd" in mm/dd/yyyy
    dd = ['01','02','03','04','05','06','07','08','09','10',
          '11','12','13','14','15','16','17','18','19','20',
          '21','22','23','24','25','26','27','28','29','30',
          '31']
    day = date[3] + date[4]
    if day in dd:
        pass
    else:
        print('Error: The Day value should be [01,...,31].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    # Testing "yyyy" in mm/dd/yyyy
    yyyy = ['2022','2023','2024','2025','2026','2027','2028',
            '2029','2030','2031','2032','2033','2034','2035']
    year = date[6] + date[7] + date[8] + date[9]
    if year in yyyy:
        pass
    else:
        print('Error: The Year value should be [2022,...,2035].')
        date = input('Please repeat input: ')
        date = cyrillic_presence_test(date, message_cyrillic)
        date = remove_tabs_and_whitespaces(date) # Remove "\t" and " ".
        date = empty_date(date)
        if date == '': return date
    return date


def get_date(date):
    """Current date for Poland if argument == ''."""
    if date == '':
        date = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting current date.
    else:
        date = date_validation(date) # Validation.
    return date


def number_validation(number, max_number):
    """Number validation in interval [1, max_number]."""
    number = cyrillic_presence_test(number, message_cyrillic)
    number = remove_tabs_and_whitespaces(number)
    if number.isdigit(): # Only decimal digits.
        number = int(number)
    else:
        print(f'Error: The item number shold be decimal digit in [1, {max_number}].')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = number_validation(number, max_number) # Recursion.
    if number in range(1,max_number+1): # Only in range [1, max_number].
        pass
    else:
        print(f'Error: The item number shold be decimal digit in [1, {max_number}].')
        number = input('Please repeat input: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = number_validation(number, max_number) # Recursion.
    return number


def choose_item(item_name, item_menu):
    """Drop-down menu analog."""
    print(f'\nThe {item_name} menu table: \n') # Table's title.
    if item_name == 'Source':
        for i,item in enumerate(item_menu,start=1):
            print(i, item, end='')
        number = input('\nChoose and Input the number: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = number_validation(number, len(item_menu)) # Validation.
        number = int(number)
        return number # Output for 'Source'.
    else:
        for i,item in enumerate(item_menu,start=1):
            print(i, item)
        number = input('\nChoose and Input the number: ')
        number = cyrillic_presence_test(number, message_cyrillic)
        number = remove_tabs_and_whitespaces(number)
        number = number_validation(number, len(item_menu)) # Validation.
        number = int(number)
        return item_menu[number - 1] # If not 'Source'.


def empty_field(field):
    """"Please repeat input": if field is empty and I press
    "Enter", make the program ask me if I really want
    to leave the field empty y/n?.
    """
    field = cyrillic_presence_test(field, message_cyrillic)
    field = remove_tabs_and_whitespaces(field) # Remove "\t" and " ".
    if field == '':
        field = force_empty_field(field)
    else:
        field = valid_decimal(field)
    return field


def force_empty_field(field):
    """Empty (or current) date."""
    result = False
    result = input('Do you really want to leave this field empty (y/n)?: ')
    result = cyrillic_presence_test(result, message_cyrillic)
    result = remove_tabs(result)
    if result in ['y', 'Y']:
        field = '' 
    else:
        field = valid_decimal(field) # Go to 
    return field


def currency_validation(currency):
    """Checks if the currency's input was right."""
    currency = cyrillic_presence_test(currency)
    currency = remove_tabs(currency)
    if len(currency) < 1: # Minimum 1 character should be present.
        print('Error: To few characters inputed.')
        currency = input('Repeat Input: ')
        currency = currency_validation(currency) # Recursion.
    currency = str_valid_to_upper(currency)
    return currency


# The initial lists' block.
with open('source.txt', 'r') as f:
    source_list = []
    for x in f:
        source_list.append(x)
type_1 = [
    'Client',
    'Dealer'
    ] # 2
type_2 = [
    'Primary',
    'Dependent'
    ] # 2
type_3 = [
    'RENEWABLE',
    'LIMITED',
    'RETAIL',
    'N/A-DEALER'
    ] # 4
entity_list = [
    'Natural',
    'Legal'
    ] # 2

base_path = './clients_base.csv' # The relative path to clients_base file.
time_zone = 'GMT+2' # Time zone for Poland.

# The clients' input loop.
i = 'y'
while i != 'q':
    os.system('cls') # Clearing the Screen.
    #The Greeting & information.
    print('Hello Host! \nYou run version 00.05 of clientsbase.py program.')
    print('Please input the Data of the new Client.')
    print('\nFull Path to clients_base.csv file is: \n' 
          + os.path.abspath(base_path) 
          + '\n')

    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    cid = cid_validation(cid) # Validation.

    first_name = input('FirstName: ')
    first_name = remove_cyrillic_and_tabs(first_name, message_cyrillic)

    last_name_1 = input('LastName1: ')
    last_name_1 = remove_cyrillic_and_tabs(last_name_1, message_cyrillic)

    last_name_2 = input('LastName2: ')
    last_name_2 = remove_cyrillic_and_tabs(last_name_2, message_cyrillic)

    middle_names = input('MiddleName: ')
    middle_names = remove_cyrillic_and_tabs(middle_names, message_cyrillic)

    source = choose_item('Source', source_list)
    
    rate_agnostic = input('RateAgnostic: ')
    rate_agnostic = one_or_zero(rate_agnostic) # Validation

    phone_number = input('PhoneNumber: ') # Phone input and validation.
    phone_number = empty_phone_number(phone_number)

    type1 = choose_item('Type1', type_1)
    type2 = choose_item('Type2', type_2)
    type3 = choose_item('Type3', type_3)
    entity = choose_item('Entity', entity_list)

    dependent = input('Dependent: ') 
    dependent = empty_field(dependent) # Full validation.
    
    base_currency = input('BaseCurrency: ')
    base_currency = currency_validation(base_currency) # Validation.

    home_address = input('HomeAddress: ')
    home_address = remove_cyrillic_and_tabs(home_address, message_cyrillic)

    telegram_name1 = input('TelegramName1: ')
    telegram_name1 = remove_cyrillic_and_tabs(telegram_name1,
                                              message_cyrillic)

    telegram_name2 = input('TelegramName2: ')
    telegram_name2 = remove_cyrillic_and_tabs(telegram_name2,
                                              message_cyrillic)

    facebook_link1 = input('FacebookLink1: ')
    facebook_link1 = remove_cyrillic_and_tabs(facebook_link1,
                                              message_cyrillic)

    facebook_link2 = input('FacebookLink2: ')
    facebook_link2 = remove_cyrillic_and_tabs(facebook_link2,
                                              message_cyrillic)

    instagram_link1 = input('InstagramLink1: ')
    instagram_link1 = remove_cyrillic_and_tabs(instagram_link1,
                                              message_cyrillic)

    instagram_link2 = input('InstagramLink2: ')
    instagram_link2 = remove_cyrillic_and_tabs(instagram_link2,
                                              message_cyrillic)

    city = input('City: ' )
    city = remove_cyrillic_and_tabs(city, message_cyrillic)

    country = input('Country: ' )
    country = remove_cyrillic_and_tabs(country, message_cyrillic)

    comments = input('Comments: ' )
    comments = remove_cyrillic_and_tabs(comments, message_cyrillic)

    # Input the 'DateAdded' manualy or get from Inet.
    date_added = input('DateAdded: ')
    date_added = get_date(date_added)

    # clients_base.csv file data:
    # fields names:
    fields = [
            'CID',
            'FirstName',
            'LastName1',
            'LastName2',
            'MiddleName',
            'Source',
            'RateAgnostic',
            'PhoneNumber',
            'Type1',
            'Type2',
            'Type3',
            'Entity',
            'Dependent',
            'BaseCurrency',
            'HomeAddress',
            'DateAdded',
            'TelegramName1',
            'TelegramName2',
            'FacebookLink1',
            'FacebookLink2',
            'InstagramLink1',
            'InstagramLink2',
            'City',
            'Country',
            'Comments'
            ]
    # Fields values.
    row = [
        cid,
        first_name,
        last_name_1,
        last_name_2,
        middle_names,
        source,
        rate_agnostic,
        phone_number,
        type1,
        type2,
        type3,
        entity,
        dependent,
        base_currency,
        home_address,
        date_added,
        telegram_name1,
        telegram_name2,
        facebook_link1,
        facebook_link2,
        instagram_link1,
        instagram_link2,
        city,
        country,
        comments
        ]

    # Checking the clients_base.csv file existing
    # and writing to clients_base.csv file.
    path = Path(base_path)
    result = path.is_file()

    if result == True:
        with open(base_path, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(base_path, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('\nInput another client data? (Press "q" to exit, \
"Enter" to continue): ')
    i = cyrillic_presence_test(i, message_cyrillic)
    i = remove_tabs_and_whitespaces(i)

input('Click "ENTER" to exit: ')
