# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable for the file to save and the path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Initialize Total Vote Counter.
total_votes = 0
# Complete List of Candidates and Votes Cast
candidate_options = []
candidate_votes = {}
# Winning Candidate, Vote Count and Percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the Total Vote Count
        total_votes += 1
        # Print candidate names from each row.
        candidate_name = row[2]
        # If Candidate name is unique add to list
        if candidate_name not in candidate_options:
            # Add candidate name to candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count.
            candidate_votes [candidate_name] = 0      
        # Add a vote to candidate's count
        candidate_votes [candidate_name] += 1

# Save results to text file
with open(file_to_save,"w") as txt_file:
    #Print the final vote count to terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes : {total_votes:,}]\n"
        f"----------------------------\n")
    print (election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Calulate Candidate Vote Count
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their vote count, and percentage to the terminal.
        print(candidate_results)
        # Save candidate results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, percentage and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print winning candidate's results to terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print (winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # 3. Print the total votes.
    #print (total_votes)

            # print(row)

        # Print the file object.
        #  print(election_data)

    
    #file_to_load = 'Resources/election_results.csv'

    """#  Open the election analysis and write to the file
    with open(file_to_save, "w") as txt_file:
        # Write three counties to the file.
        txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")"""
