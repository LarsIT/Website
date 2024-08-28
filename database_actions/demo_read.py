# Recreation of image from blob out of database

import os
import sys
# Add superior folder to python-path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import private_data.mysql_login_prvt as login
import private_data.paths_prvt as paths
import mysql.connector


script_directory: str = os.path.dirname(os.path.abspath(sys.argv[0])) 

connection = mysql.connector.connect(
    host = login.host,
    user = login.user,
    password = login.password,
    database = login.database
)

# DB operations
cursor = connection.cursor()

# Sample query
select_query = "SELECT name, photo FROM detmold_demo WHERE id=1"
cursor.execute(select_query)
result = cursor.fetchone()

name: str = result[0]
blob_data: bytes = result[1]

with open(f"{script_directory}/image/{name}" + ".jpg", "wb") as outfile:
    outfile.write(blob_data)

cursor.close()
connection.close()