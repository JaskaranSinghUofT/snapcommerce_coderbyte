# Jaskaran Singh's submission for the Coderbyte challenge for Snapcommerce

# Let's define a function that prints the table given the provided schema.
def printTable (table_attributes, table):
    print (table_attributes)
    for row in table:
        print (row)

# data is a stringified table where delimiter is ';' and line_terminator is '\n'.
data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

# This is the given data
print("\n---------- The following is the raw data that we're working with ----------\n")
print(data)

# Extract the rows from the table. These "rows" will still be strings
# Note: The first row is the attributes of the table.
rows_string = data.split('\n')

# At this point, the last row will be empty due to the split, so we need to account for that (it's a trivial row)
rows_string = rows_string[0:-1]

# We're going to create the table so we can manipulate it (it's a list of lists - a 2D-Array in a sense)
table = []

# Let's create the table row by row
for current_row_string in rows_string:
    current_row = current_row_string.split(';') # Makes a list out of the string row 
    table.append(current_row) # Grow our table (append to the table list)

# Let's extract the table attributes (table column names), which is the first list
table_attributes = table[0]

# Just to clean up our table, we need to remove the table_attributes from the actual table
table = table [1:]

# Now we're ready to do parts 1-3. Before moving onto Part 1, let's print out the "Before" data 
print ("\n********** The following is the table before anything was done to the data **********\n")
printTable(table_attributes, table)


# ----------------------------- PART 1 ----------------------------- 

# At this point, we can leverage the fact that FlightCodes is the third attribute OR
# we can be a little more general by finding the attribute/column position of "FlightCodes", which should be the third positon a.k.a. index 2
index_of_flight_codes = table_attributes.index('FlightCodes')

# Get the first row's FlightCode because that's going to be our "base" and then we're going to increment by 10 accordingly
starting_flight_code = table[0][index_of_flight_codes]

# starting_flight_code is a string, we need to convert it to an integer.
# To do so, convert the string to a float, then convert that float to an int
starting_flight_code = int (float(starting_flight_code))

# Let's update all the FlightCodes and convert them into ints (we're storing them as strings though)
for row_index in range(0, len(table)):
    table[row_index][index_of_flight_codes] = str(starting_flight_code + 10*row_index)

# Before moving onto Part 2, let's print out what we did for Part 1 
print ("\n\n********** The following is the table after Part 1 **********\n")
printTable(table_attributes, table)


# ----------------------------- PART 2 ----------------------------- 
# My undestanding of this part is that we should create an entirely new column

# In Part 1, we were general and found the attribute/column position of "FlightCodes" within the table.
# Let's do that again for the "To_From" column
index_of_to_from = table_attributes.index("To_From") # Should be 3

# To add an entirely new column in the table, we need to go row by row
for row_index in range(0, len(table)):

    # Get the To_From column value of the current row
    to_from_string = table[row_index][index_of_to_from]

    # Extract the "To" and extract the "From"
    to_from_list = to_from_string.split("_")

    # We know index 0 of to_from_list is the "To" and index 1 is the "From"
    # Convert both to upper case
    to_uppercase = to_from_list[0].upper()
    from_uppercase = to_from_list[1].upper()

    table[row_index][-1] = to_uppercase # The existing To_From column is going to be the "To" column
    table[row_index].append(from_uppercase) # Add a new column, which is the "From"


# The table attributes need to be updated to account for the column changes we made
table_attributes[-1] = "To"
table_attributes.append("From")

# Before moving onto Part 3, let's print out what we did for Part 2
print ("\n\n********** The following is the table after Part 2 **********\n")
printTable(table_attributes, table)


# ----------------------------- PART 3 ----------------------------- 

# In Part 2, we were general and found the attribute/column position of "To_From" within the table.
# This time around, let's just use the fact that the "Airline Code" column is at index 0
index_of_airline_code = 0

# Go row by row cleaning up the column
for row_index in range(0, len(table)):

    # What do we need to clean? Get that string (Airline Code)
    need_to_clean = table[row_index][index_of_airline_code]

    # Going to need a new string to append to. Start empty.
    cleaned_up = ""

    # Go through the string character-by-character
    for current_character in need_to_clean:

        # If the character is valid, then take it
        if current_character.isalpha() or current_character.isspace():
            cleaned_up = cleaned_up + current_character # Append to the cleaned_up string
    
    # We could have a bunch of spaces in the beginning or the end, so strip those all away
    cleaned_up = cleaned_up.strip()

    # Update the column
    table[row_index][index_of_airline_code] = cleaned_up

# Before joining everything back into a stringified table, let's print out what we did for Part 3
print ("\n\n********** The following is the table after Part 3 **********\n")
printTable(table_attributes, table)


# ----------------------------- Joining table back to one string ----------------------------- 

# Going to need a variable to store the stringified table
table_stringified = ""

# Go row by row and append to the stringified table
for current_row in table:
    current_row = ";".join(current_row) # Convert the current row into one string separating columns using ";"
    table_stringified = table_stringified + current_row + "\n" # Grow the string

# We need to add the table attributes to the stringified table
table_attributes_stringified = ";".join(table_attributes) # Same as above, really
new_data = table_attributes_stringified + "\n" + table_stringified

# Print the final answer!
print("\n\n---------- The following is the stringified table after Part 3  ----------\n")
print(new_data)