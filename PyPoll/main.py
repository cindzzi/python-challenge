import os
import csv

csvpath=os.path.join('..','PyPoll','election_data.csv')
#declaring variables
totalVotes= 0
khanVotes= 0
correyVotes= 0
liVotes= 0
otooleyVotes= 0
with open(csvpath, newline="")as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    csv_reader = next(csvreader)

    for row in csvreader:
        totalVotes +=1
       # print(totalVotes)

        if row[2]== "Khan":
            khanVotes +=1
        elif row[2] =="Correy":
            correyVotes +=1
        elif row[2] == "Li":
            liVotes +=1
        elif row[2] =="O'Tooley":
            otooleyVotes +=1

#create a dictionary/list 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khanVotes, correyVotes, liVotes, otooleyVotes]


    