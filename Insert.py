import Functions.InsertBinders as InsertBinders

import sqlalchemy # with admin privileges: "python -m pip install sqlalchemy pyodbc" // without admin use virtualenv
import csv

# example credentials
SERVER_NAME = "DESKTOP-1CE11ME\\SQLEXPRESS"
DATABASE_NAME = "turniej_siatkowki"
DATABASE_DRIVER = "SQL Server Native Client 11.0" # control panel>Systems and Security>Administrative Tools>ODBC Data Sources>drivers tab
DATABASE_DRIVER = DATABASE_DRIVER.replace(' ', '+')

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

def insert(dbConnection, metaData, filePath, tableName, bindingFunction):
    with open(filePath, 'r', encoding="utf8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            bindedValues = bindingFunction(row)

            table = sqlalchemy.Table(tableName, metaData, autoload=True, autoload_with=dbConnection)
            query = table.insert().values(bindedValues)
            dbConnection.execute(query)

def main():
    connectionString = "mssql+pyodbc://{}/{}?driver={}".format(SERVER_NAME, DATABASE_NAME, DATABASE_DRIVER)
    dbEngine = sqlalchemy.create_engine(connectionString)

    with dbEngine.connect() as connection:
        metaData = sqlalchemy.MetaData(dbEngine)

        insert(connection, metaData, GENERATED_DATA_DIR + '/' + CITIES_OUTPUT, "miasta", InsertBinders.cityBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + PEOPLES_OUTPUT, "osoby", InsertBinders.personBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + PLAYERS_POSITIONS_OUTPUT, "pozycje", InsertBinders.playerPositionBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + PLAYERS_OUTPUT, "zawodnicy", InsertBinders.playerBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + TEAMS_OUTPUT, "druzyny", InsertBinders.teamBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + COACHES_OUTPUT, "trenerzy", InsertBinders.coachBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + TEAM_PLAYERS_OUTPUT, "zawodnicy_druzyny", InsertBinders.teamPlayerBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + REFEREES_OUTPUT, "sedziowie", InsertBinders.refereeBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + TOURNAMENTS_OUTPUT, "turnieje", InsertBinders.tournamentBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + MATCHES_OUTPUT, "mecze", InsertBinders.matchBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + MATCH_RESULTS_OUTPUT, "wyniki_meczow", InsertBinders.matchResultBind)

if __name__ == "__main__":
    main()