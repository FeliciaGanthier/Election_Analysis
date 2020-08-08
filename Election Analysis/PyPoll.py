# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    # for row in file_reader:
        # print(row)

    # Print the file object.
    #  print(election_data)

"""
     # To do: perform analysis.
     print(election_data)
     """
  
#file_to_load = 'Resources/election_results.csv'

"""#  Open the election analysis and write to the file
with open(file_to_save, "w") as txt_file:
     # Write three counties to the file.
     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")"""
