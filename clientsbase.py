""" WollPay Clients Base (Version 00.03) """

import datetime
import pytz
import csv
import os
from pathlib import Path


def str_valid_to_upper(str_to_valid):
    """ String validation.
    Capital letters only. No numbers.
    str_to_valid  parametr (Input string to validation).
    """
    str_to_valid = remove_whitespaces(str_to_valid)

    if str_to_valid.isalpha():
        pass
    else:
        print('Error: Only letters without spaces \
are allowed in this field!')
        str_to_valid = input('Please repeat input: ')
        str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.

    str_to_valid = str_to_valid.upper()

    return str_to_valid  


def phone_number_validation(number):
    """Phone number validation.
    Sign '+' allowed on the first position.
    """
    number = remove_whitespaces(number)
    
    first_sign = ['+','0','1','2','3','4','5','6','7','8','9']
    if number[0] in first_sign:
        pass
    else:
        print('Error: Only decimal digits end "+" sign \
on first position are allowed in this field!')
        number = input('Please repeat input: ')
        number = phone_number_validation(number) # Recursion.

    sub_number = number[1:]
    if sub_number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits end "+" sign \
on first position are allowed in this field!')
        number = input('Please repeat input: ')
        number = phone_number_validation(number) # Recursion.

    return number


def one_or_zero(string_to_valid):
    """Only "1" or "0" are valid values to input parameter."""
    
    string_to_valid = remove_whitespaces(string_to_valid)

    if string_to_valid == "1" or string_to_valid == "0":
        pass
    else:
        print('Error: Only "1" or "0" without spaces \
are allowed in this field!')
        string_to_valid = input('Please repeat input: ')
        string_to_valid = one_or_zero(string_to_valid) # Recursion.

    return string_to_valid

    
def remove_whitespaces(string):
    """Code to remove whitespaces"""
    return string.replace(" ", "")


def valid_number_decimal(number):
    """ Number validation.
    Decimal numbers only without whitespaces.
    number - parameter (Input string to validation).
    """
    number = remove_whitespaces(number)

    if number.isdecimal():
        pass
    else:
        print('Error: Only decimal digits \
are allowed in this field!')
        number = input('Please repeat input: ')
        number = valid_number_decimal(number) # Recursion.
    return number    


def check_letters(str):
    """Checking for absence of letters in given string."""
    result = True # Initializing result variable.
    for i in str:
        if i.isalpha(): # if string has letter:
            result = False
    return result


def date_validation(date):
    """ Date validation.
    date - parameter (Inputed date to validation).
    """
    date = remove_whitespaces(date) # To remove whitespaces.
    
    # Testing the length of the field.
    if len(date) == 10:
        pass
    else:
        print('Error: In this field should be 10 characters.')
        date = input('Please repeat input: ')
        date = date_validation(date) # Recursion.
    
    # Testing the absence of alphabetical letters.
    if check_letters(date):
        pass
    else:
        print('Error: No letters are allowed in this field!')
        date = input('Please repeat input: ')
        date = date_validation(date) # Recursion.

    #Testing the presence of two "/" characters.
    if date[2] == date[5] == '/':
        pass
    else:
        print('Error: Check the presence of "/" characters in right places!')
        date = input('Please repeat input: ')
        date = date_validation(date) # Recursion.

    # Testing "mm" in mm/dd/yyyy
    mm = ['01','02','03','04','05','06','07','08','09','10','11','12']
    month = date[0] + date[1]
    if month in mm:
        pass
    else:
        print('Error: The Month value should be [01,...,12].')
        date = input('Please repeat input: ')
        date = date_validation(date) # Recursion.

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
        date = date_validation(date) # Recursion.
    
    # Testing "yyyy" in mm/dd/yyyy
    yyyy = ['2022','2023','2024','2025','2026','2027','2028',
            '2029','2030','2031','2032','2033','2034','2035']
    year = date[6] + date[7] + date[8] + date[9]
    if year in yyyy:
        pass
    else:
        print('Error: The Year value should be [2022,...,2035].')
        date = input('Please repeat input: ')
        date = date_validation(date) # Recursion.
    
    return date


def number_validation(number, max_number):
    """Validation"""
    if number in range(1,max_number+1):
        pass
    else:
        print(f'Error: The item number shold be decimal digit in [1, {max_number}].')
        number = input('Please repeat input: ')
        number = int(number)
        number = number_validation(number, max_number) # Recursion.
    return number


def choose_item(item_name, item_menu):
    """Drop-down menu analog."""
    print(f'\nThe {item_name} menu table: \n')
    for i,item in enumerate(item_menu,start=1):
        print(i, item)
    number = input('\nChoose and Input the number: ')
    number = int(number)
    number = number_validation(number, len(item_menu))
    return item_menu[number - 1]


# The initial lists' block.
source_list = [
    'Facebook group "Russians in Poland"',
    '"Russians in Wroclaw" Aidar\'s chat',
    'Colleague from Work',
    '"Russians in Poland" chat',
    'WollPay channel',
    '"Russians and Belarusians in Poland"',
    '"Russians in Poland Community" Telegram chat',
    'Personal matter',
    'Friends'
    ]
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
    'N/A - DEALER'
    ] # 4
entity_list = [
    'Natural',
    'Legal'
    ] # 2

base_name = './clients_base.csv' # The relative path to clients_base file.
time_zone = 'GMT+2' # Time zone for Poland.

# The clients' input loop.
i = 'y'
while i != 'q':
    os.system('cls') # Clearing the Screen.

    #The Greeting & information.
    print('Hello Host! \nYou run version 00.03 of program with partly validation.')
    print('Please input the Data of the new Client.')
    print('\nFull Path to clients_base.csv file is: \n' 
          + os.path.abspath(base_name) 
          + '\n')
    
    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    cid = valid_number_decimal(cid) # Validation.
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    middle_names = input('Middle Name: ')
    source = choose_item('Source', source_list)
    rate_agnostic = input('RateAgnostic: ')
    rate_agnostic = one_or_zero(rate_agnostic) # Validation
    phone_number = input('PhoneNumber: ')
    phone_number = phone_number_validation(phone_number) # Validation.
    type1 = choose_item('Type1', type_1)
    type2 = choose_item('Type2', type_2)
    type3 = choose_item('Type3', type_3)
    entity = choose_item('Entity', entity_list)
    dependent = input('Dependent: ')
    dependent = valid_number_decimal(dependent) # Validation.
    base_currency = input('Basecurrency: ')
    base_currency = str_valid_to_upper(base_currency) # Validation.
    home_address = input('Home Address: ')
    telegram_name1 = input('TelegramName1: ')
    telegram_name2 = input('TelegramName2: ')
    facebook_link1 = input('FacebookLink1: ')
    facebook_link2 = input('FacebookLink2: ')
    instagram_link1 = input('InstagramLink1: ')
    instagram_link2 = input('InstagramLink2: ')
    city = input('City: ' )
    country = input('Country: ' )
    comments = input('Comments: ' )

    # Input the 'DateAdded' manualy or get from Inet.
    date_added = input('DateAdded: ')
    if len(date_added) < 2:
        date_added = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting date from Inet.
    else:
        date_added = date_validation(date_added) # Validation.

    # clients_base.csv file data:
    # fields names:
    fields = [
            'CID',
            'First Name',
            'Last Name',
            'Middle Name',
            'Source',
            'RateAgnostic',
            'PhoneNumber',
            'Type1',
            'Type2',
            'Type3',
            'Entity',
            'Dependent',
            'Basecurrency',
            'Home Address',
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
        last_name,
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
    path = Path(base_name)
    result = path.is_file()

    if result == True:
        with open(base_name, 'a', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(row)
    else:
        with open(base_name, 'w', encoding='UTF8', newline='') as f:
            csvwriter = csv.writer(f, dialect='excel')
            csvwriter.writerow(fields) # Writing the fields.
            csvwriter.writerow(row)
    
    i = input('\nInput another Client? (Press "q" to exit, \
"Enter" to continue): ')

input('Click "ENTER" to exit: ')
