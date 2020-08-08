#Colorado Election Audit
#1. The total number of votes cast
#2. Complete list of candidates who recieved votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of the election basedon popular vote

import csv
import os

# Assign a variable for the file to load the path.
file_to_load = 'Resources/Test.csv'

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Print the file object.
     print(election_data)
