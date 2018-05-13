import datetime

class City:
    def __init__(self):
        self.id = 0
        self.name = ""

    def __iter__(self):
        return iter([self.id, self.name])

class Person:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""
        self.birthDate = 0
        self.salary = 0
        self.roleId = 0

    def __iter__(self):
        return iter([self.id, self.name, self.surname, self.birthDate, self.salary, self.roleId])

class PlayerPosition:
    def __init__(self):
        self.id = 0
        self.name = ""

    def __iter__(self):
        return iter([self.id, self.name])

class Team:
    def __init__(self):
        self.id = 0
        self.name = 0
        self.cityId = 0

    def __iter__(self):
        return iter([self.id, self.name, self.cityId])

class TeamPlayer:
    def __init__(self):
        self.playerId = 0
        self.teamId = 0
        self.contractStartDate = datetime.date.today()
        self.contractEndDate = datetime.date.today()

    def __iter__(self):
        return iter([self.playerId, self.teamId, self.contractStartDate, self.contractEndDate])

class Match:
    def __init__(self):
        self.id = 0
        self.team1Id = 0
        self.team2Id = 0
        self.cityId = 0
        self.refereeId = 0
        self.date = datetime.date.today()

    def __iter__(self):
        return iter([self.id, self.team1Id, self.team2Id, self.cityId,
                     self.refereeId, self.date])

class MatchResult:
    def __init__(self):
        self.matchId = 0
        self.winnerId = 0
        self.points = 0

    def __iter__(self):
        return iter([self.matchId, self.winnerId, self.points])
