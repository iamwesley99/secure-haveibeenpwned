import hashlib # used for password hashing
import requests # (NOT A PYTHON STANDARD LIBRARY, MUST DOWNLOAD)
                # this is used to get content from pwnedpasswords api
                # go to : http://docs.python-requests.org/en/latest/ ... to get Requests library

my_password = input('\n Enter a Password : ')

# creates the hash object with the sha-1 algorithm
# by passing in the enocded version of my_password(its string of bytes)
# note: the hashing function (sha1) only takes a bytes as its param
hash_object = hashlib.sha1(my_password.encode())

# creates a hex representation of the password 
hashed_password = hash_object.hexdigest()

# retreive the first 5 characters,
# used to pass into the haveibeenpwned address
first_bits = hashed_password[:5]

# pulls the byte version from the API and converts each line to an array
r       = requests.get('https://api.pwnedpasswords.com/range/' + first_bits)
r_array = r.content.decode('UTF-8').splitlines()

# the test string does not include the first 5 characters
# because the API does not return those characters as it is not necessary
test_string = hashed_password[5:40].upper()
found_match = False
occurences  = ""

# loops through r_array and tests for finding
for counter, str in enumerate(r_array):
    if str[:35] == test_string:
        found_match = True
        occurences = str[36:]

        
# Final print messages
if found_match:
    print('\n ' + my_password + ' was found')
    print(' Hash : ' + hashed_password + ' ... ' + occurences + ' occurences\n')
else:
    print('\n Password not found!\n')

# Author  : Wesley Witter (On github: iamwesley99)
# email   : wesleywitter1@gmail.com
