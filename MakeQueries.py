import Functions.QueryBinders as InsertBinders

import csv
import argparse

DB_NAME = "turniej_siatkowki"

GENERATED_DATA_DIR = "output"
QUERY_OUTPUT = "DaneTabel.sql"

CITIES_OUTPUT = "cities.txt"
PLAYERS_POSITIONS_OUTPUT = "playerPositions.txt"
PEOPLES_OUTPUT = "peoples.txt"
TEAMS_OUTPUT = "teams.txt"
TEAM_PLAYERS_OUTPUT = "teamPlayers.txt"
MATCHES_OUTPUT = "matches.txt"
MATCH_RESULTS_OUTPUT = "matchResults.txt"

QrBeg = "INSERT INTO "

CITIES_QUERY = QrBeg + "miasta (id, nazwa) VALUES "
PLAYERS_POSITIONS_QUERY = QrBeg + "role (id, nazwa) VALUES "
PEOPLES_QUERY = QrBeg + "osoby (id, imie, nazwisko, data_ur, pensja, id_roli) VALUES "
TEAMS_QUERY = QrBeg + "druzyny (id, nazwa, id_miasta) VALUES "
TEAM_PLAYERS_QUERY = QrBeg + "osoby_druzyny (id_osoby, id_druzyny, poczatek_kontraktu, koniec_kontraktu) VALUES "
MATCHES_QUERY = QrBeg + "mecze (id, id_druzyny_1, id_druzyny_2, id_miasta, id_sedziego, data_meczu) VALUES "
MATCH_RESULTS_QUERY = QrBeg + "wyniki (id_meczu, zwyciezca, punkty) VALUES "

QUERY_IDENTITY_ON = ["SET IDENTITY_INSERT miasta ON;",
                    "SET IDENTITY_INSERT role ON;",
                    "SET IDENTITY_INSERT osoby ON;",
                    "SET IDENTITY_INSERT druzyny ON;",
                    "",
                    "SET IDENTITY_INSERT mecze ON;",
                    ""]

QUERY_IDENTITY_OFF = ["SET IDENTITY_INSERT miasta OFF;",
                    "SET IDENTITY_INSERT role OFF;",
                    "SET IDENTITY_INSERT osoby OFF;",
                    "SET IDENTITY_INSERT druzyny OFF;",
                    "",
                    "SET IDENTITY_INSERT mecze OFF;",
                    ""]

def insert(tableQuery, filePath, tableName, bindingFunction, onIdInsert, offIdInsert):
    queryString = onIdInsert
    queryString += "\n" + tableQuery
    with open(filePath, 'r', encoding="utf8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            bindedValues = bindingFunction(row)
            queryString += "\n" + bindedValues + ","
    
    queryString = queryString[:-1] # remove last ','
    queryString += ";"
    queryString += "\n" + offIdInsert
    return queryString

def main():
    queryFileContent = "USE " + DB_NAME + "\nGO"

    queryFileContent += "\n\n" + insert(CITIES_QUERY, GENERATED_DATA_DIR + '/' + CITIES_OUTPUT, "miasta", InsertBinders.cityBind, QUERY_IDENTITY_ON[0], QUERY_IDENTITY_OFF[0])
    queryFileContent += "\n\n" + insert(PLAYERS_POSITIONS_QUERY, GENERATED_DATA_DIR + '/' + PLAYERS_POSITIONS_OUTPUT, "role", InsertBinders.playerPositionBind, QUERY_IDENTITY_ON[1], QUERY_IDENTITY_OFF[1])
    queryFileContent += "\n\n" + insert(PEOPLES_QUERY, GENERATED_DATA_DIR + '/' + PEOPLES_OUTPUT, "osoby", InsertBinders.personBind, QUERY_IDENTITY_ON[2], QUERY_IDENTITY_OFF[2])
    queryFileContent += "\n\n" + insert(TEAMS_QUERY, GENERATED_DATA_DIR + '/' + TEAMS_OUTPUT, "druzyny", InsertBinders.teamBind, QUERY_IDENTITY_ON[3], QUERY_IDENTITY_OFF[3])
    queryFileContent += "\n\n" + insert(TEAM_PLAYERS_QUERY, GENERATED_DATA_DIR + '/' + TEAM_PLAYERS_OUTPUT, "osoby_druzyny", InsertBinders.teamPlayerBind, QUERY_IDENTITY_ON[4], QUERY_IDENTITY_OFF[4])
    queryFileContent += "\n\n" + insert(MATCHES_QUERY, GENERATED_DATA_DIR + '/' + MATCHES_OUTPUT, "mecze", InsertBinders.matchBind, QUERY_IDENTITY_ON[5], QUERY_IDENTITY_OFF[5])
    queryFileContent += "\n\n" + insert(MATCH_RESULTS_QUERY, GENERATED_DATA_DIR + '/' + MATCH_RESULTS_OUTPUT, "wyniki", InsertBinders.matchResultBind, QUERY_IDENTITY_ON[6], QUERY_IDENTITY_OFF[6])

    queryFileContent += "\nGO"

    filePath = GENERATED_DATA_DIR + "/" + QUERY_OUTPUT
    with open(filePath, 'w', encoding="utf8") as queryFile:
        queryFile.write(queryFileContent)
        queryFile.flush()

if __name__ == "__main__":
    main()