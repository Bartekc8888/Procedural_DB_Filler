
def cityBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["nazwa"] = listOfValues[1]

    return dictionary

def playerPositionBind(listOfValues):
    return cityBind(listOfValues)

def personBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["imie"] = listOfValues[1]
    dictionary["nazwisko"] = listOfValues[2]
    dictionary["data_ur"] = listOfValues[3]
    dictionary["pensja"] = listOfValues[4]

    return dictionary

def playerBind(listOfValues):
    dictionary = {}
    dictionary["id_osoby"] = listOfValues[0]
    dictionary["id_pozycji"] = listOfValues[1]

    return dictionary

def teamBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["nazwa"] = listOfValues[1]
    dictionary["id_miasta"] = listOfValues[2]

    return dictionary

def coachBind(listOfValues):
    dictionary = {}
    dictionary["id_osoby"] = listOfValues[0]
    dictionary["id_druzyny"] = listOfValues[1]
    dictionary["poczatek_karery"] = listOfValues[2] ## TODO fix generation

    return dictionary

def teamPlayerBind(listOfValues):
    dictionary = {}
    dictionary["id_osoby"] = listOfValues[0]
    dictionary["id_druzyny"] = listOfValues[1]
    dictionary["numer_koszulki"] = listOfValues[2]
    dictionary["poczatek_kontraktu"] = listOfValues[3]
    dictionary["koniec_kontraktu"] = listOfValues[4]

    return dictionary

def refereeBind(listOfValues):
    dictionary = {}
    dictionary["id_osoby"] = listOfValues[0]
    dictionary["ranga_zawodow"] = listOfValues[1]
    dictionary["stanowisko"] = listOfValues[2]

    return dictionary

def tournamentBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["ranga"] = listOfValues[1]
    dictionary["nazwa"] = listOfValues[2]

    return dictionary

def matchBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["id_turnieju"] = listOfValues[1]
    dictionary["id_druzyny_1"] = listOfValues[2]
    dictionary["id_druzyny_2"] = listOfValues[3]
    dictionary["id_miasta"] = listOfValues[4]
    dictionary["id_sedziego_1"] = listOfValues[5]
    dictionary["id_sedziego_2"] = listOfValues[6]
    dictionary["id_sedziego_3"] = listOfValues[7]
    dictionary["data_meczu"] = listOfValues[8]
    return dictionary


def matchResultBind(listOfValues):
    dictionary = {}
    dictionary["id_meczu"] = listOfValues[0]
    dictionary["id_zwyciezcy"] = listOfValues[1]
    dictionary["punkty"] = listOfValues[2]

    return dictionary