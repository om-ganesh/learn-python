import sqlite3

def write_json_to_sqlite(tbl_data, dbName):
    
    print('Creating a Db record: ' + dbName)
    result = []
    #1.Connect to the db
    try:
        dbConnection = sqlite3.connect(dbName)

        #2. Create table
        dbConnection.execute("""
            CREATE TABLE IF NOT EXISTS tbl_measurements (
            id INTEGER PRIMARY KEY,
            weight FLOAT,
            temperature FLOAT,
            color VARCHAR(32),
            recorded_on DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)

        #3. Create a sql insert query
        insert_sql = 'INSERT INTO tbl_measurements (weight, temperature, color) values(?, ?, ?)'

        #4. Execute the query
        for measurement in tbl_data:
            dbConnection.execute(insert_sql, 
                (measurement['weight']
                , measurement['temperature']
                , measurement['color'])
                )
        dbConnection.commit()

    except (sqlite3.Error, sqlite3.Warning) as error:
        print(error)
        return None
    finally:
        dbConnection.close()
    print('Data successfully recorded')

def read_from_sqlite(dbName):
    
    print('Reading a Db record: ' + dbName)
    result = []
    #1.Connect to the db
    try:
        dbConnection = sqlite3.connect(dbName)
        
        #2. Display the records from table
        tbl_data = dbConnection.execute('SELECT * FROM tbl_measurements')
        for row in tbl_data:
            result.append(row)
    except (sqlite3.Error, sqlite3.Warning) as error:
        print(error)
        return None
    finally:
        dbConnection.close()
    return result