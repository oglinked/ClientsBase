""" WollPay Clients Base (Version 00.01) """

# import random
import datetime
# from datetime import date
import pytz
import csv
from pathlib import Path
import os


# def str_valid_to_upper(str_to_valid):
#     """ String validation.
#     Capital letters only. No numbers.
#     str_to_valid  parametr (Input string to validation).
#     """
#     if str_to_valid.isalpha():
#         pass
#     else:
#         print('Error: Only letters without spaces \
# are allowed in this field!')
#         # print(f'Your input was "{str_to_valid}".')
#         str_to_valid = input('Please repeat input: ')
#         str_to_valid = str_valid_to_upper(str_to_valid) # Recursion.
#     str_to_valid = str_to_valid.upper()
#     return str_to_valid  


# def isfloat(num):
#     """Python Program to Check If a String Is a Number (Float)"""
#     try:
#         float(num)
#         return True
#     except ValueError:
#         return False
    

# def valid_number(number):
#     """ Number validation.
#     Numbers only. Dots are allowed to float numbers.
#     number - parametr (Input string to validation).
#     """
#     if number.isdecimal():
#         pass
#     elif isfloat(number):
#         pass
#     else:
#         print('Error: Only decimal digits (and one dot) \
# are allowed in this field!')
#         number = input('Please repeat input: ')
#         number = valid_number(number) # Recursion.
#     return number    


def remove_whitespaces(string):
    """Code to remove whitespaces"""
    return string.replace(" ", "")


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


base_name = './clients_base.csv' # The relative path to clients_base file.
time_zone = 'GMT+2' # Time zone for Poland.

# The clients' input loop.
i = 'y'
while i != 'q':
    os.system('cls') # Clearing the Screen.

    #The Greeting & information.
    print('Hello Host! You run version 00.01 of program.')
    print('Please input the Data of the new Client.')
    print('\nFull Path to clients_base.csv file is: \n' 
          + os.path.abspath(base_name) 
          + '\n')
    
    # The Input Data Block with partly Validation.
    cid = input('CID: ')
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    middle_names = input('Middle Name: ')
    source = input('Source: ')
    rate_agnostic = input('RateAgnostic: ')
    phone_number = input('PhoneNumber: ')
    type1 = input('Type1: ')
    type2 = input('Type2: ')
    type3 = input('Type3: ')
    entity = input('Entity: ')
    dependent = input('Dependent: ')
    base_currency = input('Basecurrency: ')
    home_address = input('Home Address: ')
    telegram_name1 = input('TelegramName1: ')
    telegram_name2 = input('TelegramName2: ')
    city = input('City: ' )
    country = input('Country: ' )
    comments = input('Comments: ' )

    # Input the 'DateAdded' manualy or get from Inet.
    date_added = input('DateAdded: ')
    if len(date_added) < 2:
        date_added = datetime.datetime.now(pytz.timezone('Poland')) \
                       .strftime("%m/%d/%Y") # Getting date from Inet.
    else:
        date_added = date_validation(date_added)

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
