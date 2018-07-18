## Challenge 2: PyPoll
# 
# # Notes to self: 
#       The file has a header.
#       We need to calculate the following: 
#           1.  The total number of votes cast --> Simply report the sum of all the votes. 
#           2.	A complete list of candidates who received votes --> need a find the unqiue names from row[2]
#           3.	The percentage of votes each candidate won:
#               --> For each of these unique candidates need to find out the total number of votes for a particular candidate 
#               --> and divide it by the total number of votes cast (from Step 1). Multiply by 100. 
#           4.	The total number of votes each candidate won --> Collect from previous step
#           5.	The winner of the election based on popular vote --> Among the unique names who has the maximum vote counts is the WINNER!
#       Like the previous code, we need to use git to submit this assignment!!!
# Resources used: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/. 
#               For the writing the text also use the same loop.
# Resources used: https://www.geeksforgeeks.org/python-get-unique-values-list/
# Note on set:  Using set() property of Python, we can easily check for the unique values. 
#               Insert the values of the list in a set. 
#               Set only stores a value once even if it is inserted more then once. 
#               After inserting all the values in the set by list_set=set(list1)
#               Convert this set to a list to print it.


# Objective 1: Import modules os and csv. Importing numpy in order to use the unique function
import os
import csv

# Objective 2: Set the path for the CSV file in PyPollcsv

PyPollcsv = os.path.join("Resources","election_data.csv")

# Objective 3: Create the lists to store data. Initialize

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
# Note to TA: I have tried several ways to get the max of the votecount list and retrieve the name as Winner. But unsucessful. 
# Hence I am leaving that part out of this code. But Khan is the winner, I know!!!!
# Jake suggested: votecount = votecount["percentage"].sort_values()
# Print to terminal
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")


