import Functions.DataStructures as DataStructures
import Functions.GenerationFunctions as GenerationFunctions

import random
import datetime
import csv
import os
import argparse

GENERATION_DATA_DIR = "GeneratorData"

CITIES_FILE_NAME = "cities.txt"
MALE_NAMES_FILE_NAME = "firstMaleNames.txt"
LAST_NAMES_FILE_NAME = "lastNames.txt" 
PLAYER_POSITIONS_FILE_NAME = "playerPositions.txt"
TEAM_NAMES_FILE_NAME = "teamNames.txt"

GENERATED_DATA_DIR = "output"

CITIES_OUTPUT = "cities.txt"
PEOPLES_OUTPUT = "peoples.txt"
PLAYERS_POSITIONS_OUTPUT = "playerPositions.txt"
PLAYERS_OUTPUT = "players.txt"
TEAMS_OUTPUT = "teams.txt"
TEAM_PLAYERS_OUTPUT = "teamPlayers.txt"
MATCHES_OUTPUT = "matches.txt"
MATCH_RESULTS_OUTPUT = "matchResults.txt"

NUMBER_OF_TEAMS_TO_GENERATE = 10
REFEREES_NUMBER = 5

citiesNames, maleNames, surnames, playerPositionsNames, teamNames = ([] for i in range(5))
cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults = ([] for i in range(9))

def loadDataFromFile(filePath):
    with open(filePath, encoding="utf8") as file:
        lines = file.read().splitlines()
        return lines

def writeGeneratedDataToFile(filePath, data):
    with open(filePath, "w", newline='', encoding="utf8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)

def getmatchingReferees():
    referee = random.choice(referees)
    
    return referee

def initGenerationData():
    global citiesNames, maleNames, surnames, playerPositionsNames, teamNames

    citiesNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + CITIES_FILE_NAME)
    maleNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + MALE_NAMES_FILE_NAME)
    surnames = loadDataFromFile(GENERATION_DATA_DIR + '/' + LAST_NAMES_FILE_NAME)
    playerPositionsNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + PLAYER_POSITIONS_FILE_NAME)
    teamNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + TEAM_NAMES_FILE_NAME)

def createTeams():
    global cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults

    for teamCounter in range(NUMBER_OF_TEAMS_TO_GENERATE):
        teamId = teamCounter + 1
        teams.append(GenerationFunctions.generateTeam(teamId, teamNames, cities))

        numberOfPlayersInTeam = random.randint(6, 11)
        peoplesCount = len(peoples)
        for playerId in range(numberOfPlayersInTeam):
            personId = peoplesCount + playerId + 1
            peoples.append(GenerationFunctions.generatePerson(personId, maleNames, surnames, playerPositionsNames, False))
            
            teamPlayers.append(GenerationFunctions.generateTeamPlayer(personId, teamId))

        coachId = len(peoples) + 1
        peoples.append(GenerationFunctions.generatePerson(coachId, maleNames, surnames, playerPositionsNames, True))
        coaches.append(GenerationFunctions.generateCoach(peoples[-1], teamId))
        teamPlayers.append(GenerationFunctions.generateTeamPlayer(coachId, teamId))

def createReferees():
    global cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults

    peoplesCount = len(peoples)
    for refereeCounter in range(REFEREES_NUMBER):
        personId = peoplesCount + 1 + refereeCounter
        peoples.append(GenerationFunctions.generatePerson(personId, maleNames, surnames, playerPositionsNames, True))
        referees.append(GenerationFunctions.generateReferee(peoples[-1]))

def createTournaments():
    global cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults

    startDate = GenerationFunctions.randomDate(datetime.date.today() - datetime.timedelta(days=5*365), datetime.date.today() - datetime.timedelta(days=120))
    endDate = startDate + datetime.timedelta(days=65)

    matchesCount = len(matches)
    for matchCounter in range(len(teams)):
        for opponentCounter in range(len(teams)):
            if matchCounter == opponentCounter:
                continue
            
            matchId = matchesCount + matchCounter * len(teams) + opponentCounter + 1
            refs = getmatchingReferees()

            matches.append(GenerationFunctions.generateMatch(matchId, teams[matchCounter], teams[opponentCounter],
                                                            refs.id, startDate, endDate))
            matchResults.append(GenerationFunctions.generateMatchResult(matches[-1]))

def generateData():
    global cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults

    cities = GenerationFunctions.generateCities(citiesNames)
    playerPositions = GenerationFunctions.generatePlayerPositions(playerPositionsNames)

    createTeams()
    createReferees()
    createTournaments()

def writeData():
    global cities, peoples, playerPositions, teams, coaches, teamPlayers, referees, matches, matchResults

    if not os.path.exists(GENERATED_DATA_DIR):
        os.makedirs(GENERATED_DATA_DIR)

    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + CITIES_OUTPUT, cities)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + PEOPLES_OUTPUT, peoples)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + PLAYERS_POSITIONS_OUTPUT, playerPositions)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + TEAMS_OUTPUT, teams)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + TEAM_PLAYERS_OUTPUT, teamPlayers)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + MATCHES_OUTPUT, matches)
    writeGeneratedDataToFile(GENERATED_DATA_DIR + '/' + MATCH_RESULTS_OUTPUT, matchResults)

def main():
    global NUMBER_OF_TEAMS_TO_GENERATE, REFEREES_NUMBER

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--teams", help="number of team to generate", type=int)
    parser.add_argument("-r", "--referees", help="number of referees to generate", type=int)
    
    args = parser.parse_args()
    if args.teams and args.teams > 1:
        NUMBER_OF_TEAMS_TO_GENERATE = args.teams
    if args.referees and args.referees > 0:
        REFEREES_NUMBER = args.tournaments

    initGenerationData()
    generateData()
    writeData()

if __name__ == "__main__":
    main()