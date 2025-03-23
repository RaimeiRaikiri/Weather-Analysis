import sqlite3
# Once a day
    # Take in data from an API

# Create database 
def create_database():
    connection = sqlite3.connect("rainham_weather.db")
    cursor = connection.cursor()

    cursor.execute(""" 
                CREATE TABLE IF NOT EXISTS rainham_weather(
                    id INTEGER PRIMARY KEY,
                    temperature FLOAT NOT NULL,
                    date DATE NOT NULL
                )
                """)


def extract_data(connection) -> list[tuple[float, str]]:
    cursor = connection.cursor()
    cursor.execute("SELECT")
    return 

def linear_regression(historical_data):
    pass

def find_average_temperature(historical_data):
    pass

def find_minmimum_temperature(historical_data):
    pass

def find_maximum_temperature(historical_data):
    pass



create_database()