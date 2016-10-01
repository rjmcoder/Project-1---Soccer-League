import csv

def createTeams():
  Sharks = []
  Dragons = []
  Raptors = []
  expPlayers = 0
  regPlayers = 0
  
  with open('projectFile.txt', newline='') as csvfile:
    teamReader = csv.DictReader(csvfile, delimiter=',')
    rows = list(teamReader)
        
    # divide the team equally
    for row in rows:
      if row['Soccer Experience'] == 'YES':
        if expPlayers % 3 == 0:
          expPlayers += 1
          Sharks.append(row)
        elif expPlayers % 3 == 1:
          expPlayers += 1
          Dragons.append(row)
        elif expPlayers % 3 == 2:
          expPlayers += 1
          Raptors.append(row)
      else:
        if regPlayers % 3 == 0:
          regPlayers += 1
          Sharks.append(row)
        elif regPlayers % 3 == 1:
          regPlayers += 1
          Dragons.append(row)
        elif regPlayers % 3 == 2:
          regPlayers += 1
          Raptors.append(row)
    
    # create letters
    for player in Dragons:
      timeOfPractice = "March 17 at 1pm"
      createLetter(player, 'Dragons', timeOfPractice)
      
    for player in Sharks:
      timeOfPractice = "March 17 at 3pm"
      createLetter(player, 'Sharks', timeOfPractice)
    
    for player in Raptors:
      timeOfPractice = "March 18 at 1pm"
      createLetter(player, 'Raptors', timeOfPractice)
      
      
def createLetter(nameDict, team, timeOfPractice):
  fileName = nameDict['Name'].split()[0] + "_" + nameDict['Name'].split()[1] + ".txt"
  with open(fileName, 'w') as f:
    letter = """Dear {},\n
We are happy and excited to let you know that your child {} has been selected to play in our {} team. We would like to invite you to join your's child's first team practice on {}.\n
Thanks and see you there.""".format(nameDict['Guardian Name(s)'], nameDict['Name'], team, timeOfPractice)
    f.write(letter)
  
    
if __name__ == "__main__":
  createTeams()