# Insertion of demo data

import os
import sys
# Add superior folder to python-path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Website.private_data.mysql_login_prvt as login
import Website.private_data.paths_prvt as paths
import mysql.connector


connection = mysql.connector.connect(
    host = login.host,
    user = login.user,
    password = login.password,
    database = login.database
)

def convert_to_blob(file_path: str) -> bytes:
    with open(file_path, "rb") as file:
        blob = file.read()
        return blob


image_folder = paths.image_folder
i: int = 0
data: list= []

for pic in os.listdir(image_folder):
    i += 1
    name = pic[:-4]
    blob = convert_to_blob(image_folder + "/" + pic)
    data.append((i, name, blob))
        
# DB operations
cursor = connection.cursor()

insert_query = """INSERT INTO detmold_demo (id, name, photo) VALUES (%s, %s, %s)"""

cursor.executemany(insert_query, data)
connection.commit()

cursor.close()
connection.close()


