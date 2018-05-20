
def cityBind(listOfValues):
    return "(" + listOfValues[0] + ", '" + listOfValues[1] + "')"

def playerPositionBind(listOfValues):
    return cityBind(listOfValues)

def personBind(listOfValues):
    return "(" + listOfValues[0] + ", '" + listOfValues[1] + "', '" + listOfValues[2] + "', '" + \
            listOfValues[3] + "', " + listOfValues[4] + ", " + listOfValues[5] + ")"

def teamBind(listOfValues):
    return "(" + listOfValues[0] + ", '" + listOfValues[1] + "', " + listOfValues[2] + ")"

def teamPlayerBind(listOfValues):
    return "(" + listOfValues[0] + ", " + listOfValues[1] + ", '" + listOfValues[2] + "', '" + listOfValues[3] + "')"

def matchBind(listOfValues):
    return "(" + listOfValues[0] + ", " + listOfValues[1] + ", " + listOfValues[2] + ", " + \
            listOfValues[3] + ", " + listOfValues[4] + ", '" + listOfValues[5] + "')"

def matchResultBind(listOfValues):
    return "(" + listOfValues[0] + ", " + listOfValues[1] + ", " + listOfValues[2] + ")"