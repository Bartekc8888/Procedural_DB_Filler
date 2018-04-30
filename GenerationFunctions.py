import DataStructures
import random
import datetime
from typing import List

def generateCities(citiesNames : List[str]):
    citiesList = []

    for name in citiesNames:
        citiesList.append(DataStructures.City())
        id = len(citiesList)
        citiesList[id].id = id
        citiesList[id].name = name

    return citiesList

def generatePerson(personId : int, maleNames : List[str], surnames : List[str]):
    person = DataStructures.Person()
    person.id = personId
    person.name = random.choice(maleNames)
    person.surname = random.choice(surnames)
    person.age = random.randint(18, 35)
    person.salary = random.randint(2100, 3200)

    return person

def generatePlayerPositions(positionNames : List[str]):
    positionsList = []

    for name in positionNames:
        positionsList.append(DataStructures.PlayerPosition())
        id = len(positionsList)
        positionsList[id].id = id
        positionsList[id].name = name
    
    return positionNames

def generatePlayer(personId : int, positions : List[DataStructures.PlayerPosition]):
    player = DataStructures.Player()
    player.personId = personId
    player.playerPositionId = random.choice(positions).id

    return player

def generateTeam(teamId : int, teamNames : List[str], cities : List[DataStructures.City]):
    team = DataStructures.Team()
    team.personId = teamId
    team.name = random.choice(teamNames)
    team.cityId = random.choice(cities).id

    return team

def randomDate(start, end):
    delta = end - start
    int_delta = delta.total_seconds()
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def generateTeamPlayer(playerId : int, teamId : int):
    teamPlayer = DataStructures.TeamPlayer()
    teamPlayer.playerId = playerId
    teamPlayer.teamId = teamId
    teamPlayer.tshirtNumber = random.randint(1, 99) # TODO make no duplicates of t-shirt number

    dateStart = datetime.date.today() - datetime.timedelta(days=3*365)
    dateEnd = datetime.date.today() - datetime.timedelta(days=1)

    teamPlayer.contractStartDate = randomDate(dateStart, dateEnd)

    dateStart = datetime.date.today() + datetime.timedelta(days=180)
    dateEnd = datetime.date.today() + datetime.timedelta(days=5*365)

    teamPlayer.contractEndDate = randomDate(dateStart, dateEnd)

    return teamPlayer

def generateReferee(personId : int, teamId : int, refereePositions : List[str]):
    referee = DataStructures.Referee()
    referee.personId = personId
    referee.teamId = teamId
    referee.experienceInYears = random.randint(2, 31)
    referee.refereePosition = random.choice(refereePositions)

    return referee

def generateTournament(tournamentId : int, tournamentNames : List[str], tournamentRanks : List[str]):
    tournament = DataStructures.Tournament()
    tournament.id = tournamentId
    tournament.name = random.choice(tournamentNames)
    tournament.rank = random.choice(tournamentRanks)

    return tournament

def generateMatch(matchId : int, tournamentId : int, team1 : DataStructures.Team, team2 : DataStructures.Team, referee1Id : int, referee2Id : int, referee3Id : int, startDate, endDate):
    match = DataStructures.Match()
    match.id = matchId
    match.tournamentId = tournamentId
    match.team1Id = team1.id
    match.team2Id = team2.id
    match.cityId = team1.cityId
    match.referee1Id = referee1Id
    match.referee2Id = referee2Id
    match.referee3Id = referee3Id
    match.date = randomDate(startDate, endDate)

    return match

def generateMatchResult(match : DataStructures.Match):
    matchResult = DataStructures.MatchResult()
    matchResult.matchId = match.id
    if random.choice([True, False]):
        matchResult.winnerId = match.team1Id
    else:
        matchResult.winnerId = match.team2Id
    matchResult.points = random.randint(2, 6)

    return matchResult

