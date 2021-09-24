# -*- coding: utf-8 -*-
"""

@author: sonamariya
"""

import sqlite3


# =============================================================================
# Connecting and Creating a new SQLite database
# =============================================================================


conn = sqlite3.connect('Hollywood.db')

print("created database successfully");


# =============================================================================
# Creating a new table (Movies)
# =============================================================================


conn.execute('''CREATE TABLE Movie
          (ID INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
          Director       TEXT     NOT NULL,
          ACTOR        CHAR(50),
          ACTRESS        CHAR(50),
          year_of_release        CHAR(50));''')
          
          
print("Table created successfully");



# =============================================================================
# Inserting data into Movies table
# =============================================================================


conn.execute("INSERT INTO Movie (ID,NAME,Director,ACTOR,ACTRESS,year_of_release) \
      VALUES (1, 'Inception', 'Christopher Nolan', 'Leonardo DiCaprio', 'Elliot Page', '2010')");

conn.execute("INSERT INTO Movie (ID,NAME,Director,ACTOR,ACTRESS,year_of_release) \
      VALUES (2, 'Iron Man 3', 'Jon Favreau', 'Robert Downey Jr', 'Gwyneth Kate Paltrow', '2013')");

conn.execute("INSERT INTO Movie (ID,NAME,Director,ACTOR,ACTRESS,year_of_release) \
      VALUES (3, 'spiderman', 'Sam Raimi', 'Tobey Maguire', 'Kirsten Dunst', '2002')");

conn.execute("INSERT INTO Movie (ID,NAME,Director,ACTOR,ACTRESS,year_of_release) \
      VALUES (4, 'Avatar', 'James Cameron', 'Sam Worthington', 'Zoe Saldana', '2009')");
      
      
conn.commit()
print("Records created successfully");



cur = conn.cursor();

# =============================================================================
# Querying data from Movies table
# =============================================================================

print("\n selecting all records \n");
for row in cur.execute('SELECT * FROM Movie ORDER BY NAME'):
        print(row)
        
        
print("\n selecting records based on  movie name\n");      
for row in cur.execute('SELECT * FROM Movie where NAME ="Avatar"'):
          print(row)
        
print("\n selecting all records where actor is Leonardo DiCaprio \n");      
for row in cur.execute('SELECT * FROM Movie where ACTOR ="Leonardo DiCaprio"'):
          print(row)
        

