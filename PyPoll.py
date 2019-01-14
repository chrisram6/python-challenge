import os
import csv

filename = "election_data.csv"

numVotes = 0
candidates = []
index=""

match = False

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        numVotes+=1
        candidates.append(row[2])

#add the first candidate to the unique candidates list
unique_votee = []
unique_votee.append(candidates[0])

#sort only unique candidates into the "uniqueCand" list
for candidate in candidates:
    for each in unique_votee:
        if each == candidate:
            match=True
            break
    if match==True:
        match=False
        continue
    else:
        unique_votee.append(candidate)

#calculate how many votes each one got
voterList=[]
for each in unique_votee:
    voterList.append(0)

for idx,each in enumerate(unique_votee):
    for candidate in candidates:
        if candidate==each:
            voterList[idx]+=1

#Calculate each candidate's percent won + number of votes won
percentList = []

for votes in voterList:
    percent = round(((votes/numVotes)*100),2)
    percentList.append(percent)

#Find out who's the winner
first_place = 0
for idx,votes in enumerate(voterList):
    if int(votes) > first_place:
        first_place = int(votes)
        index = idx
winner = unique_votee[index]


print(f"Election Results\n-----------------\nTotal Votes:{numVotes}")
print(f"-----------------")
for idx,candidate in enumerate(unique_votee):
    print(f"{candidate}: {percentList[idx]}% ({voterList[idx]})")
print(f"-----------------\nWinner: {winner}")
print("-----------------")

file = open("PyPollResults.txt", 'w')

file.write(f"Election Results\n-----------------\n")
file.write(f"Total Votes: {numVotes}\n-----------------\n")
for idx,candidate in enumerate(unique_votee):
    file.write(f"{candidate}: {percentList[idx]}% ({voterList[idx]})\n")
file.write(f"-----------------\nWinner: {winner}\n")
file.write("-----------------")
