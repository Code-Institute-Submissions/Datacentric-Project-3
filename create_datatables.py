import os
import pymysql

# database username
username = 'sql12317054'

# database host
hostname = 'sql12.freemysqlhosting.net'

# database = password
password = 'i4HZtC2C6y'

# database name
db_name = 'sql12317054'

# declare a list containing all the create table sql syntax
sql = [
    
'''CREATE TABLE Users (user_id INTEGER AUTO_INCREMENT PRIMARY KEY, name varchar(255) NOT NULL UNIQUE);''',
    
'''CREATE TABLE Manufacturer (manufacturer_id INTEGER AUTO_INCREMENT PRIMARY KEY, manufacturer_description varchar(100) NOT NULL UNIQUE);''',

'''CREATE TABLE Type (type_id INTEGER AUTO_INCREMENT PRIMARY KEY, cereals_type varchar(10) NOT NULL);''', 

'''CREATE TABLE Cereals (cereal_id INTEGER AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), manufacturer_id INTEGER, FOREIGN KEY (manufacturer_id) REFERENCES Manufacturer (manufacturer_id),
type_id INTEGER, FOREIGN KEY (type_id) REFERENCES Type (type_id), calories INTEGER, protein INTEGER, fat INTEGER, sodium INTEGER, fiber INTEGER, carbohyrates INTEGER,
sugars INTEGER, potassium INTEGER, vitamins INTEGER, ratings INTEGER, review_count INTEGER);''',

'''CREATE TABLE Ratings (rating_id INTEGER AUTO_INCREMENT PRIMARY KEY, ratings INTEGER, comment VARCHAR(255), user_id INTEGER, FOREIGN KEY (user_id) REFERENCES Users (user_id),
cereal_id INTEGER, FOREIGN KEY (cereal_id) REFERENCES Cereals (cereal_id));'''


]

try:
    
    # try to establish the connection to the database
    try: 
        connection = pymysql.connect(host=hostname, user=username, password=password, db=db_name)
    except pymysql.MySQLError as e:
        # print out the error
        print(f"Connection is not successful. Encountered error: {e}")
        
    with connection.cursor() as cursor:
        for tables in sql:
            cursor.execute(tables)

finally:
    # close the connection to the database
    connection.close(); 