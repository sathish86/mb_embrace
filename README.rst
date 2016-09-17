#################
MB Python library
#################

Steps:

Step1:
Need to setup two environmental variables.

PYTHONPATH='/<project_path>'
MB_SETTINGS_MODULE='local_settings'


Assumption:


Task 1:
1. Used GOOGLE MAP API (2500 request per day) to find the GEO coordinates of a location and using these information
    it finds the restaurant details based cuisine type from Factual API by distance in ascending order.

Task2:

1. This POST request doesn't have any authentication details from the document, so this app doesn't check authentication.
2. This App finds (most to least) common match of the group members, it loop through using below logic.
    a. Using set intersect, it tries to find most common of all the group members, if no common data found then
    b. It eliminate the last person from the group and tries to intersect with remaining group members,
    c. It loop through until find common item from the group or until only one person left in the group.
3. It also uses GOOGLE MAP API GEO coordinates of the given location.
4. For logging purpose, this app stores the post request information in a table using sqllite.
  In production system, I prefer to use Postgres DB.


