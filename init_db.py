import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Connecting...")
try:
    conn = mysql.connector.connect(
            host='192.168.3.7',
            user='root',
            password='python'
      )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('User or password incorrect')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `gamebrary`;")

cursor.execute("CREATE DATABASE `gamebrary`;")

cursor.execute("USE `gamebrary`;")

# creating tables
TABLES = {}
TABLES['Games'] = ('''
      CREATE TABLE `games` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `gamename` varchar(50) NOT NULL,
      `category` varchar(40) NOT NULL,
      `console` varchar(20) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Users'] = ('''
      CREATE TABLE `users` (
      `username` varchar(20) NOT NULL,
      `nick` varchar(20) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`nick`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
      table_sql = TABLES[table_name]
      try:
            print('Creating table {}:'.format(table_name), end=' ')
            cursor.execute(table_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Already Exists!')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserting users
user_sql = 'INSERT INTO users (username, nick, password) VALUES (%s, %s, %s)'
users = [
      ('Pedro', 'pedro', generate_password_hash('venus').decode('utf-8')),
      ('Costa', 'costa', generate_password_hash('saturno').decode('utf-8')),
      ('Almeida', 'almeida', generate_password_hash('plutao').decode('utf-8'))
]
cursor.executemany(user_sql, users)

cursor.execute('select * from gamebrary.users')
print(' -------------  Users:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserting games
games_sql = 'INSERT INTO games (gamename, category, console) VALUES (%s, %s, %s)'
games = [
      ('Tetris', 'Puzzle', 'Atari'),
      ('God of War', 'Hack n Slash', 'PS2'),
      ('Mortal Kombat', 'Luta', 'PS2'),
      ('Crash Bandicoot', 'Hack n Slash', 'PS2'),
      ('Need for Speed', 'Corrida', 'PS2'),
]
cursor.executemany(games_sql, games)

cursor.execute('select * from gamebrary.games')
print(' -------------  games:  -------------')
for game in cursor.fetchall():
    print(game[1])


#commiting changes
conn.commit()
cursor.close()
conn.close()