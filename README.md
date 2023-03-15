# Meeting room booking
    #### Video Demo:  <URL HERE>
    #### Description:  A command-line program to book meetings rooms in an office building

## Project considerations
In this project I combined several of the skills from earlier submissions in the cource.
Keeping within the scope of CS50p, I used a 1-dimentional csv-file as data-storage instead of an database like Sqlite. So in this project the booking times are singular, instead od multiple, for each date pr. room.

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

<tab>-New Room-<br>
From Date: 2023-03-16 12:00<br>
To Date: 2023-03-16 12:30<br>

-Available Rooms-<br>
+--------+------------+<br>
|   Room |   Capacity |<br>
+========+============+<br>
|    101 |          4 |<br>
+--------+------------+<br>
|    102 |          8 |<br>
+--------+------------+<br>
|    401 |         22 |<br>
+--------+------------+<br>
Select Room Number: 102<br>

2 "Remove Booking": Same as 'New Booking', but removing selected room as 'Occupied'.<br>
3 "Available Rooms": Lists all non occupied rooms.<br>
4 "Occupied Rooms": Listes all occupied rooms.<br>
5 "All Rooms": Lists a 'raw' list of all rooms, available and occupied.<br>
6 "Save & Exit": Saved changes to the csv-file and existes the program.<br>



