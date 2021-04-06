import csv

csvpath = "Resources/election_data.csv"
#Define and set variables
Candidate_list = []
count = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
#Create a list of all occurences for each candidate and total number of votes
    for row in csvreader:
        count = count + 1
        Candidate_list.append(row[2])
  
#Count how many times each candidate occurs in the candidate list    
    Khan_count = Candidate_list.count("Khan")
    Correy_count = Candidate_list.count("Correy")
    Li_count = Candidate_list.count("Li")
    Otooley_count = Candidate_list.count("O'Tooley")

#Formulas for % of votes for each candidate
    kp = round((Khan_count/count)*100, 2)
    cp = round((Correy_count/count)*100, 2)
    lp = round((Li_count/count)*100, 2)
    op = round((Otooley_count/count)*100, 2)



    
print("Election Results")
print("-------------------------")  
print(f"Total Votes: {count}")  
print("-------------------------") 
print(f"Khan: {kp}% ({Khan_count})")
print(f"Correy: {cp}% ({Correy_count})")
print(f"Li: {lp}% ({Li_count})")
print(f"O'Tooley: {op}% ({Otooley_count})")
print("-------------------------") 
print("Winner: Khan")
print("-------------------------")
    
with open("output.txt", "w") as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Votes: {count}\n")
    text.write("-------------------------\n")
    text.write(f"Khan: {kp}% ({Khan_count})\n")
    text.write(f"Correy: {cp}% ({Correy_count})\n")
    text.write(f"Li: {lp}% ({Li_count})\n")
    text.write(f"O'Tooley: {op}% ({Otooley_count})\n")
    text.write("-------------------------\n")
    text.write("Winner: Khan\n")
    text.write("-------------------------")