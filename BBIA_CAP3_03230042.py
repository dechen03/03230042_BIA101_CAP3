#https://github.com/dechen03/03230042_BIA101_CAP3
# Dechen Dorji
# BBI 'A'
# 03230042

#References
#https://www.geeksforgeeks.org/extract-numbers-from-a-text-file-and-add-them-using-python/
#https://www.geeksforgeeks.org/python-extract-numbers-from-string/
#https://docs.python.org/3/tutorial/errors.html

# Solution
# Total sum < 478841>


#This function read the input file and fine the total solution
def read_input(filename):
    #setting sum totall as 0
    sum_total=0
    #Will try this code
    try:
        # Opening the file for reading .With will open the file and close the file. 
        with open(filename,'r') as file:
            #reading file line by line
            for line in file:
                # strip() will remove leading and trailing whitespace characters from the line
                line = line.strip()
                # If the line is not empty
                if line:
                   # Calling the function extract_number(line)
                    number = extract_number(line)
                    # add sum_total and number
                    sum_total+= number
    # After trying the code if the input file is not found this code will run                 
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    # If there is other error this code will run   
    except Exception as error:
        print(f"There is an '{error}', Please check your code")
        
            
    #will return the sum total    
    return sum_total

def extract_number(line):
   #   Making an empty list to store digits found in the line
    digits = []
    # Iterate over every character in the line
    for char in line:
        # Check if the character is number
        if char.isdigit():
            # If it is number than add it to the digits
            digits.append(char)
    # Check if the len of the digit is greater than 2 or equal 2
    if len(digits) >= 2:
        # It will get first number in the digits
        first_digit = digits[0]
        #It will get last number from the digits
        last_digit = digits[-1]
        #concatenat the first_digit and last_digit and form a new number
        
        two_number=int(first_digit + last_digit)
         # will return the new form number which is stored in the two_number
        return two_number
    #  Return 0 if there are fewer than two digits
    return 0
    
   
# This function will print the solution
def print_solution(filename):
    #  Call read_input function to get the total sum from the file
    result=read_input(filename)
    #  Print the total sum of the numbers extracted from the input file
    print('The total sum of the given input file',input_file,'is',result)
  
   
input_file=r'042.txt'
# Call the print_solution function with the input file to print the solution
print_solution(input_file)




