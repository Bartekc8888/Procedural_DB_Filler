
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
    dictionary["id_roli"] = listOfValues[5]

    return dictionary

def teamBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["nazwa"] = listOfValues[1]
    dictionary["id_miasta"] = listOfValues[2]

    return dictionary

def teamPlayerBind(listOfValues):
    dictionary = {}
    dictionary["id_osoby"] = listOfValues[0]
    dictionary["id_druzyny"] = listOfValues[1]
    dictionary["poczatek_kontraktu"] = listOfValues[2]
    dictionary["koniec_kontraktu"] = listOfValues[3]

    return dictionary

def matchBind(listOfValues):
    dictionary = {}
    dictionary["id"] = listOfValues[0]
    dictionary["id_druzyny_1"] = listOfValues[1]
    dictionary["id_druzyny_2"] = listOfValues[2]
    dictionary["id_miasta"] = listOfValues[3]
    dictionary["id_sedziego"] = listOfValues[4]
    dictionary["data_meczu"] = listOfValues[5]
    return dictionary


def matchResultBind(listOfValues):
    dictionary = {}
    dictionary["id_meczu"] = listOfValues[0]
    dictionary["zwyciezca"] = listOfValues[1]
    dictionary["punkty"] = listOfValues[2]

    return dictionary