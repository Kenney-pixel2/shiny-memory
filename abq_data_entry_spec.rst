======================================
 ABQ Data Entry Program Specification
======================================

Description
-----------
The program is being created to minimize data entry errors for laboratory measurements.

Functionality Required
----------------------

The program must:

* allow all relevant, valid data to be entered, as per the field chart
* append entered data to a CSV file
  - The CSV file must have a filename of abq_data_record_CURRENTDATE.csv,
    where CURRENTDATE is teh date of the checks in ISO format (Year-month-day)
  - The CSV file must have all the fields as per the chart
* enforce correct datatypes per field
* have inputs that:
  - ignore meaningless keystrokes
  - display an error if the value is invalid on focusout
  - display an error if a required field is empty on focusout
* prevent saving the record when errors are present

The program should try, whenever possible, to:

* enforce reasonable limits on data entered
* Auto-fill data
* Suggest likely correct values
* Provide a smooth and efficient workflow

Functionality Not Required
--------------------------

The program does not need to:

* Allow editing of data. This can be done in LibreOffice if necessary.
* Allow delettion of data.

Limitations
-----------

The program must:

* Be efficiently operable by keyboard-only users.
* Be accessible to color blind users.
* Run on Debina Linux.
* Run acceptably on a low-end PC.

Data Dictionary
---------------
+-----------+----------+-------+--------------+---------------------+
|Field      | Datatype | Units | Range        |Description          |
+===========+==========+=======+==============+=====================+
|Date       | Date     |       |              |Date of record       |
+-----------+----------+-------+--------------+---------------------+
|Time       | Time     |       | 8:00, 12:00, |Date of record       |
|           |          |       | 16:00, 20:00 |                     |
+-----------+----------+-------+--------------+---------------------+
|Lab        | String   |       | A - C        |Lab ID               |
+-----------+----------+-------+--------------+---------------------+
|Technician | String   |       | A - C        |Lab ID               |
+-----------+----------+-------+--------------+---------------------+

