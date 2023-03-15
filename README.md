# Meeting room booking
    #### Video Demo:  <URL HERE>
    #### Description:  A command-line program to book meetings rooms in an office building

## Project considerations
In this project I combined several of the skills from earlier submissions in the cource.
Keeping within the scope of CS50p, I used a 1-dimentional csv-file as data-storage instead of an database like Sqlite. So in this project the booking times are singular, instead of multiple, for each date pr. room.

## Code files
<b>project.py</b> is the start file and contains main(), start_menu() and other test def`s.<br>
<b>rooms.py</b> contains det Rooms object and associated functions like room sorting and views.<br>
<b>csv_work.py</b> contains the functions that reDA nd writes to the csv-file. The exception is printit() that print all the list using [tabulate](https://pypi.org/project/tabulate/).<br>
<b>teat_project.py</b> contains all the tests for project.py

## Using the program
The program startst with typing "python3 project.py" in the command-prompt.
This will display the "Meeting Room Booking" menu that opt for selecting a number value from the listed menu. 

-Meeting Room Booking-<br>
[1] New Booking<br>
[2] Remove Booking<br>
[3] Available Rooms<br>
[4] Occupied Rooms<br>
[5] All Rooms<br>
[6] Save & Exit<br>

1 "New Booking": Takes the user thrue selecting dates ("From" - "To"), displaying available rooms, and selecting a listed room number. When done the change is saved and reflected thrue the different "views" in menu selection 3-5.

-New Room-<br>
From Date: 2023-03-16 12:00<br>
To Date: 2023-03-16 12:30<br>

-Available Rooms-<br>
*list of rooms*<br>

Select Room Number: 202<br>


2 "Remove Booking": Same as 'New Booking', but removing selected room as 'Occupied'.
3 "Available Rooms": Lists all non occupied rooms.
4 "Occupied Rooms": Listes all occupied rooms.
5 "All Rooms": Lists a 'raw' list of all rooms, available and occupied.
6 "Save & Exit": Saved changes to the csv-file and existes the program.
