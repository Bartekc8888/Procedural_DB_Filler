import Functions.DataStructures as DataStructures
import random
import datetime
from typing import List

def generateCities(citiesNames : List[str]):
    citiesList = []

    for name in citiesNames:
        citiesList.append(DataStructures.City())
        id = len(citiesList)
        citiesList[id - 1].id = id
        citiesList[id - 1].name = name

    return citiesList

def generatePerson(personId : int, maleNames : List[str], surnames : List[str], roles : List[str], isOld : bool):
    person = DataStructures.Person()
    person.id = personId
    person.name = random.choice(maleNames)
    person.surname = random.choice(surnames)
    person.roleId = random.randint(2, len(roles))

    age = 0
    if isOld:
        age = random.randint(30, 65)
    else:
        age = random.randint(18, 35)

    birthDate = datetime.date.today() - datetime.timedelta(days=age*365)
    birthDate = randomDate(birthDate, birthDate + datetime.timedelta(days=365))
    person.birthDate = birthDate
    person.salary = random.randint(2100, 3200)

    return person

def generatePlayerPositions(positionNames : List[str]):
    positionsList = []

    positionsList.append(DataStructures.PlayerPosition())
    positionsList[0].id = 1
    positionsList[0].name = "Trener"
    positionsList.append(DataStructures.PlayerPosition())
    positionsList[1].id = 2
    positionsList[1].name = "Sedzia"

    for name in positionNames:
        positionsList.append(DataStructures.PlayerPosition())
        id = len(positionsList)
        positionsList[id - 1].id = id
        positionsList[id - 1].name = name
    
    return positionsList

def generateTeam(teamId : int, teamNames : List[str], cities : List[DataStructures.City]):
    team = DataStructures.Team()
    team.id = teamId
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

    dateStart = datetime.date.today() - datetime.timedelta(days=3*365)
    dateEnd = datetime.date.today() - datetime.timedelta(days=1)

    teamPlayer.contractStartDate = randomDate(dateStart, dateEnd)

    dateStart = datetime.date.today() + datetime.timedelta(days=180)
    dateEnd = datetime.date.today() + datetime.timedelta(days=5*365)

    teamPlayer.contractEndDate = randomDate(dateStart, dateEnd)

    return teamPlayer

def generateCoach(person, teamId : int):
    person.salary = person.salary + 1400 
    person.birthDate = person.birthDate - datetime.timedelta(days=10*365)
    person.roleId = 1

    generateTeamPlayer(person.id, teamId)

    return person

def generateReferee(person):
    person.roleId = 2

    return person

def generateMatch(matchId : int, team1 : DataStructures.Team, team2 : DataStructures.Team, refereeId : int, startDate, endDate):
    match = DataStructures.Match()
    match.id = matchId
    match.team1Id = team1.id
    match.team2Id = team2.id
    match.cityId = team1.cityId
    match.refereeId = refereeId
    match.date = randomDate(startDate, endDate)

    return match

def generateMatchResult(match : DataStructures.Match):
    matchResult = DataStructures.MatchResult()
    matchResult.matchId = match.id
    if random.choice([True, False]):
        matchResult.winnerId = match.team1Id
    else:
        matchResult.winnerId = match.team2Id
    matchResult.points = random.randint(2, 5)

    return matchResult

