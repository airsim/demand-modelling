from sets import Set

############################### MAIN  ###################################
input_file = open ('flight_numbers.txt')
lines = input_file.readlines()
flight_list = {}

# Parse the lines and build the list of flight numbers
for i in lines:
    airline_code, flight_number = i[0:-1].split(' ')
    if airline_code not in flight_list:
        flight_list[airline_code] = Set()
    numbers = flight_list[airline_code]
    numbers.add (flight_number)

sorted_codes = flight_list.keys()
sorted_codes.sort()
for code in sorted_codes:
    numbers = flight_list[code]
    sorted_numbers = sorted(numbers)
    for number in sorted_numbers:
        print code, number



