from percentDiff import *

while True:
    user_string1 = input("Enter String 1: ")
    user_string2 = input("Enter String 2: ")
    percent = percentDiff(user_string1, user_string2)
    print ("The two strings are %",percent,"similar.")
