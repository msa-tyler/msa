import os.path
import statistics

def get_file_name():
    while True:
        #prompt user to enter file name
        user_input = input("Please enter a file name: ")
        #make sure user entered a value. Re prompt if not
        if user_input == "":
            print("ERROR: please enter a value.\n")
            continue
        elif not os.path.exists(user_input):
            print("ERROR: File does not exist.\n")
            continue
        else:
            break
    #else return the value
    return user_input

#Function to load numbers from file into list
#Parameters: file name
#returns a list of numbers
def load_numbers_list(file_name):
    numbers_list = []
    #open the file
    file = open(file_name, "r")
    #read file line by line
    for number in file:
        #convert to int and append numbers to a list
        numbers_list.append(int(number))
    #return the list
    return numbers_list

def calculate_median_value(numbers_list):
    #sort the list
    numbers_list.sort()
    #determine if the list has an even or odd number of items using the len() function
    if (len(numbers_list) % 2 == 0):
        is_even = True
    else:
        is_even = False
    #if even find the two middle values and calculate the average of the two
    if is_even:
        index_1 = int(len(numbers_list) / 2)
        print(index_1)
        index_2 = index_1 - 1
        print(index_2)
        median = (numbers_list[index_1] + numbers_list[index_2]) / 2
    #if odd, return the middle value
    else:
        index = int((len(numbers_list) - 1) / 2)
        median = numbers_list[index]
 
    return median

def determine_modal_value(numbers_list):
    modal_values = {}
    list_of_modal_values = []
    for number in numbers_list:
        if number in modal_values:
            modal_values[number] += 1
        else:
            modal_values[number] = 1
    list_values = modal_values.values()
    max_value = max(list_values)
    for key in modal_values:
        if modal_values[key] == max_value:
            list_of_modal_values.append(key)
    return list_of_modal_values

def determineRange(numbers_list):
    return max(numbers_list)-min(numbers_list)

def determineMean(numbers_list):
    return statistics.mean(numbers_list)

def determineMin(numbers_list):
    return min(numbers_list)

def determineMax(numbers_list):
    return max(numbers_list)

def determineCount(numbers_list):
    return len(numbers_list) 

def determineSum(numbers_list):
    return sum(numbers_list)




def main():
    #ask user to enter filename and open that file
    file_name = get_file_name()
    
    #load number from file into a list
    list_of_numbers = load_numbers_list(file_name)

    #check the length of the list
    if len(list_of_numbers) == 0:
        print("File was empty")
    elif len(list_of_numbers) == 1:
        print("Only one number in file")
    else:
        print(f"File name:{file_name}")
        median = calculate_median_value(list_of_numbers)
        print(f"Median:{median}")
        mode = determine_modal_value(list_of_numbers)
        print(f"Mode:{mode}")
        range = determineRange(list_of_numbers)
        print(f"Range:{range}")
        mean = determineMean(list_of_numbers)
        print(f"Mean:{mean}")
        min = determineMin(list_of_numbers)
        print(f"Minimum:{min}")
        max = determineMax(list_of_numbers)
        print(f"Max:{max}")
        count = determineCount(list_of_numbers)
        print(f"Count:{count}")
        sum = determineSum(list_of_numbers)
        print(f"Sum:{sum}")

        
main()