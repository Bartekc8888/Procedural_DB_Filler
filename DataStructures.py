import datetime

class City:
    def __init__(self):
        self.id = 0
        self.name = ""

class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""
        self.age = 0
        self.salary = 0

class PlayerPosition:
    def __init__(self):
        self.id = 0
        self.name = ""

class Player:
    def __init__(self):
        self.personId = 0
        self.playerPositionId = 0

class Team:
    def __init__(self):
        self.id = 0
        self.name = 0
        self.cityId = 0

class Coach:
    def __init__(self):
        self.id = 0
        self.teamId = 0
        self.experienceInYears = 0

class TeamPlayer:
    def __init__(self):
        self.teamId = 0
        self.playerId = 0
        self.tshirtNumber = 0
        self.contractStartDate = datetime.date.today()
        self.contractEndDate = datetime.date.today()

class Referee:
    def __init__(self):
        self.personId = 0
        self.tournamentRank = ""
        self.refereePosition = ""

class Tournament:
    def __init__(self):
        self.id = 0
        self.rank = ""
        self.name = ""

class Match:
    def __init__(self):
        self.id = 0
        self.tournamentId = 0
        self.team1Id = 0
        self.team2Id = 0
        self.cityId = 0
        self.referee1Id = 0
        self.referee2Id = 0
        self.referee3Id = 0
        self.date = datetime.date.today()

class MatchResult:
    def __init__(self):
        self.matchId = 0
        self.winnerId = 0
        self.points = 0
