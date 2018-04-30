import DataStructures
import GenerationFunctions

import random
import datetime

GENERATION_DATA_DIR = "GeneratorData"

CITIES_FILE_NAME = "cities.txt"
MALE_NAMES_FILE_NAME = "firstMaleNames.txt"
LAST_NAMES_FILE_NAME = "lastNames.txt" 
PLAYER_POSITIONS_FILE_NAME = "playerPositions.txt"
REFEREE_POSITIONS_FILE_NAME = "refereePositions.txt"
TEAM_NAMES_FILE_NAME = "teamNames.txt"
TOURNAMENT_NAMES_FILE_NAME = "tournamentNames.txt"
TOURNAMENT_RANKS_FILE_NAME = "tournamentRanks.txt"

GENERATED_DATA_DIR = "output"

CITIES_OUTPUT = "cities.txt"
PEOPLES_OUTPUT = "peoples.txt"
PLAYERS_POSITIONS_OUTPUT = "playerPositions.txt"
PLAYERS_OUTPUT = "players.txt"
TEAMS_OUTPUT = "teams.txt"
COACHES_OUTPUT = "coaches.txt"
TEAM_PLAYERS_OUTPUT = "teamPlayers.txt"
REFEREES_OUTPUT = "referees.txt"
TOURNAMENTS_OUTPUT = "tournaments.txt"
MATCHES_OUTPUT = "matches.txt"
MATCH_RESULTS_OUTPUT = "matchResults.txt"

NUMBER_OF_TEAMS_TO_GENERATE = 10
REFEREES_MULTIPLICATOR_NUMBER = 4 # REFEREES_MULTIPLICATOR_NUMBER * len(refereePositionsNames)
TOURNAMENTS_NUMBER = 3

citiesNames, maleNames, surnames, playerPositionsNames, refereePositionsNames, teamNames, tournamentNames, torunamentRanks = ([] for i in range(8))
cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults = ([] for i in range(11))

def loadDataFromFile(filePath):
    with open(filePath, encoding="utf8") as file:
        lines = file.read().splitlines()
        return lines

def initGenerationData():
    global citiesNames, maleNames, surnames, playerPositionsNames, refereePositionsNames, teamNames, tournamentNames, torunamentRanks

    citiesNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + CITIES_FILE_NAME)
    maleNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + MALE_NAMES_FILE_NAME)
    surnames = loadDataFromFile(GENERATION_DATA_DIR + '/' + LAST_NAMES_FILE_NAME)
    playerPositionsNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + PLAYER_POSITIONS_FILE_NAME)
    refereePositionsNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + REFEREE_POSITIONS_FILE_NAME)
    teamNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + TEAM_NAMES_FILE_NAME)
    tournamentNames = loadDataFromFile(GENERATION_DATA_DIR + '/' + TOURNAMENT_NAMES_FILE_NAME)
    torunamentRanks = loadDataFromFile(GENERATION_DATA_DIR + '/' + TOURNAMENT_RANKS_FILE_NAME)

def createTeams():
    global cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults

    for teamCounter in range(NUMBER_OF_TEAMS_TO_GENERATE):
        teamId = teamCounter + 1
        teams.append(GenerationFunctions.generateTeam(teamId, teamNames, cities))

        numberOfPlayersInTeam = random.randint(6, 11)
        usedTshirtNumbers = []
        peoplesCount = len(peoples)
        for playerId in range(numberOfPlayersInTeam):
            personId = peoplesCount + playerId + 1
            peoples.append(GenerationFunctions.generatePerson(personId, maleNames, surnames, False))
            players.append(GenerationFunctions.generatePlayer(personId, playerPositions))
            
            teamPlayers.append(GenerationFunctions.generateTeamPlayer(personId, teamId, usedTshirtNumbers))
            usedTshirtNumbers.append(teamPlayers[-1].tshirtNumber)

        coachId = len(peoples)
        peoples.append(GenerationFunctions.generatePerson(coachId, maleNames, surnames, True))
        coaches.append(GenerationFunctions.generateCoach(coachId, teamId, peoples[-1].age))

def createReferees():
    global cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults

    peoplesCount = len(peoples)
    for refereeCounter in range(REFEREES_MULTIPLICATOR_NUMBER):
        for positionCounter in range(len(refereePositionsNames)):
            personId = peoplesCount + refereeCounter * len(refereePositionsNames) + positionCounter
            peoples.append(GenerationFunctions.generatePerson(personId, maleNames, surnames, True))
            referees.append(GenerationFunctions.generateReferee(personId, torunamentRanks, refereePositionsNames))

def createTournaments():
    global cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults

    for tournamentCounter in range(TOURNAMENTS_NUMBER):
        tournamentId = tournamentCounter + 1
        tournaments.append(GenerationFunctions.generateTournament(tournamentId, tournamentNames, torunamentRanks))

        startDate = datetime.date.today() - datetime.timedelta(days=5*365)
        endDate = startDate + datetime.timedelta(days=65)

        refs = []
        
        for counter in range(len(refereePositionsNames)):
            referee = random.choice(referees)
            while referee.refereePosition != refereePositionsNames[counter]:
                #nonlocal referee
                referee = random.choice(referees)

            refs.append(referee)

        matchesCount = len(matches)
        for matchCounter in range(len(teams)):
            for opponentCounter in range(len(teams)):
                matchId = matchesCount + matchCounter + opponentCounter + 1
                matches.append(GenerationFunctions.generateMatch(matchId, tournamentId, teams[matchCounter], teams[opponentCounter],
                                                                refs[0].personId, refs[1].personId, refs[2].personId, startDate, endDate))
                matchResults.append(GenerationFunctions.generateMatchResult(matches[-1]))

def generateData():
    global cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults

    cities = GenerationFunctions.generateCities(citiesNames)
    playerPositions = GenerationFunctions.generatePlayerPositions(playerPositionsNames)

    createTeams()
    createReferees()
    createTournaments()

def writeData():
    global cities, peoples, playerPositions, players, teams, coaches, teamPlayers, referees, tournaments, matches, matchResults

    pass

def main():
    initGenerationData()
    generateData()
    writeData()

    print("TODO")

if __name__ == "__main__":
    main()