import Functions.InsertBinders as InsertBinders

import sqlalchemy # with admin privileges: "python -m pip install sqlalchemy pyodbc" // without admin use virtualenv
import pyodbc
import csv
import argparse

# example credentials
SERVER_NAME = "DESKTOP-1CE11ME\\SQLEXPRESS"
DATABASE_NAME = "turniej_siatkowki"
DATABASE_DRIVER = "SQL Server Native Client 11.0" # control panel>Systems and Security>Administrative Tools>ODBC Data Sources>drivers tab

GENERATED_DATA_DIR = "output"

CITIES_OUTPUT = "cities.txt"
PEOPLES_OUTPUT = "peoples.txt"
PLAYERS_POSITIONS_OUTPUT = "playerPositions.txt"
TEAMS_OUTPUT = "teams.txt"
TEAM_PLAYERS_OUTPUT = "teamPlayers.txt"
MATCHES_OUTPUT = "matches.txt"
MATCH_RESULTS_OUTPUT = "matchResults.txt"

def insert(dbConnection, metaData, filePath, tableName, bindingFunction):
    with open(filePath, 'r', encoding="utf8") as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            bindedValues = bindingFunction(row)

            table = sqlalchemy.Table(tableName, metaData, autoload=True, autoload_with=dbConnection)
            query = table.insert(None).values(bindedValues)
            dbConnection.execute(query)

def main():
    global SERVER_NAME, DATABASE_NAME, DATABASE_DRIVER

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", help="server name / path", type=str)
    parser.add_argument("-n", "--name", help="database name", type=str)
    parser.add_argument("-d", "--driver", help="database driver eg \"SQL Server Native Client 11.0\"", type=str)
    
    args = parser.parse_args()
    if args.server:
        SERVER_NAME = args.server
    if args.name:
        DATABASE_NAME = args.name
    if args.driver:
        DATABASE_DRIVER = args.driver
    DATABASE_DRIVER = DATABASE_DRIVER.replace(' ', '+')

    connectionString = "mssql+pyodbc://{}/{}?driver={}".format(SERVER_NAME, DATABASE_NAME, DATABASE_DRIVER)
    dbEngine = sqlalchemy.create_engine(connectionString)

    with dbEngine.connect() as connection:
        metaData = sqlalchemy.MetaData(dbEngine)

        insert(connection, metaData, GENERATED_DATA_DIR + '/' + CITIES_OUTPUT, "miasta", InsertBinders.cityBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + PLAYERS_POSITIONS_OUTPUT, "role", InsertBinders.playerPositionBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + PEOPLES_OUTPUT, "osoby", InsertBinders.personBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + TEAMS_OUTPUT, "druzyny", InsertBinders.teamBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + TEAM_PLAYERS_OUTPUT, "osoby_druzyny", InsertBinders.teamPlayerBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + MATCHES_OUTPUT, "mecze", InsertBinders.matchBind)
        insert(connection, metaData, GENERATED_DATA_DIR + '/' + MATCH_RESULTS_OUTPUT, "wyniki", InsertBinders.matchResultBind)

if __name__ == "__main__":
    main()