# Number to Words Converter (Python Console App)
#
# This program takes a number as input from the user,
# then converts each digit into its corresponding word using a dictionary.
#
# How it works:
# - User enters a number as a string
# - Each digit is read one by one
# - The program maps each digit to its word (0 → zero, 1 → one, etc.)
# - The result is printed in a single line separated by spaces
dict={'0': "zero", '1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
Entered_number=[]
Entered_number= (input("Enter Your number please : "))
for i in Entered_number:
    print(dict[i],end=" ")



