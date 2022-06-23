counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(county  +  " county has " + str(voters) + " registered voters." )


 print(election_data)


# Close the file.

election_data.close()

# Create a filename variable to a direct or inderect path to the file.

file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a text file.

with open(file_to_save,"w") as txt_file:

# Write three counties to the file.

    txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

# Close the file
txt_file.close()

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote