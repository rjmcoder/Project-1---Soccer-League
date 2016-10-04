import csv
import sys

def createTeams(*args):
  
  noOfTeams = len(args)
  teams = {}
  
  for i, arg in enumerate(args):
    teams[i] = []
    teams[i].append(arg)
    
  expPlayers = 0
  regPlayers = 0
  
  with open('projectFile.txt', newline='') as csvfile:
    teamReader = csv.DictReader(csvfile, delimiter=',')
    rows = list(teamReader)
    
    if len(rows) % len(args) != 0:
      print("Due to lack of players the teams won't be evenly distributed.")
      print("No. of Players {}, No. of Teams {}".format(len(rows), len(args)))
      sys.exit()

    # divide the team equally
    for row in rows:
      if row['Soccer Experience'] == 'YES':
        teams[expPlayers].append(row)
        expPlayers += 1
        if expPlayers >= len(args): expPlayers = 0
      else:
        teams[regPlayers].append(row)
        regPlayers += 1
        if regPlayers >= len(args): regPlayers = 0
    
    # create letters
    for i in teams:
      for idx, player in enumerate(teams[i]):
        if idx == 0 and player == "Dragons":
          team = "Dragons"
          timeOfPractice = "March 17 at 1pm"
          continue
        elif idx == 0 and player == "Sharks": 
          team = "Sharks"
          timeOfPractice = "March 17 at 3pm"
          continue
        elif idx == 0 and player == "Raptors":
          team = "Raptors"
          timeOfPractice = "March 18 at 1pm"
          continue
        elif idx == 0:            # catch-all condition
          print("**ERROR: Team not found")
          sys.exit()
        createLetter(player, team, timeOfPractice)

            
def createLetter(nameDict, team, timeOfPractice):
  fileName = nameDict['Name'].split()[0].lower() + "_" + nameDict['Name'].split()[1].lower() + ".txt"
  with open(fileName, 'w') as f:
    letter = """Dear {},\n
We are happy and excited to let you know that your child {} has been selected to play in our {} team. We would like to invite you to join your's child's first team practice on {}.\n
Thanks and see you there.""".format(nameDict['Guardian Name(s)'], nameDict['Name'], team, timeOfPractice)
    f.write(letter)
  
    
if __name__ == "__main__":
  createTeams("Dragons", "Sharks", "Raptors")