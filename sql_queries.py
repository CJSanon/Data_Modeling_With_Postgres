# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

# Fact table for our star schema
songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time TIMESTAMPTZ NOT NULL, \
                        user_id INT NOT NULL, level VARCHAR NOT NULL, song_id VARCHAR, artist_id VARCHAR, session_id INT NOT NULL, location VARCHAR NOT NULL, user_agent VARCHAR NOT NULL);"

# User dimension table which will store user data from the JSON log: log_data
user_table_create = "CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY, first_name VARCHAR NOT NULL, last_name VARCHAR NOT NULL, gender CHAR NOT NULL, level VARCHAR NOT NULL);"

# Song dimension table which will store song information from JSON log: song_data
song_table_create = "CREATE TABLE IF NOT EXISTS songs (id VARCHAR PRIMARY KEY, title VARCHAR NOT NULL, artist_id VARCHAR NOT NULL, year INT NOT NULL, duration NUMERIC NOT NULL);"

# Artist dimension table which will store artist information from JSON log: song_data
artist_table_create = "CREATE TABLE IF NOT EXISTS artists (id VARCHAR PRIMARY KEY, artist_name VARCHAR NOT NULL, artist_location text NOT NULL, artist_latitude NUMERIC, artist_longitude NUMERIC);"

# Timestamp dimension table which will store timestamps from JSON log: log_data
time_table_create = "CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMPTZ PRIMARY KEY, year INT NOT NULL, month INT NOT NULL, week INT NOT NULL, day INT NOT NULL, hour INT NOT NULL, weekday INT NOT NULL);"

# INSERT RECORDS

# Inserts data from log_data log into our sparkify database fact table: songplays
songplay_table_insert = "INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

# Inserts data from log_data log into the "users" dimension table
user_table_insert = "INSERT INTO users (id, first_name, last_name, gender, level) " \
                    "VALUES (%s, %s, %s, %s, %s) " \
                    "ON CONFLICT (id) " \
                    "DO UPDATE SET level=EXCLUDED.level"

# Inserts data from song_data log into the "songs" dimension table
song_table_insert = "INSERT INTO songs (id, title, artist_id, year, duration) " \
                    "VALUES (%s, %s, %s, %s, %s) " \
                    "ON CONFLICT (id)" \
                    "DO NOTHING" \

# Inserts data from song_data log into the "artists" dimension table
artist_table_insert = "INSERT INTO artists (id, artist_name, artist_location, artist_latitude, artist_longitude) " \
                      "VALUES (%s, %s, %s, %s, %s) " \
                      "ON CONFLICT (id) " \
                      "DO NOTHING"

# Inserts data from log_data log into the "time" dimension table
time_table_insert = "INSERT INTO time (start_time, year, month, week, day, hour, weekday) " \
                    "VALUES (%s, %s, %s, %s, %s, %s, %s) " \
                    "ON CONFLICT (start_time) " \
                    "DO NOTHING"

# FIND SONGS

# Finding the song id and artist id based on the the title, artist name, and duration of a song
song_select = "SELECT s.id song_id, a.id artist_id FROM songs s " \
              "JOIN artists a ON s.artist_id = a.id " \
              "WHERE s.title = %s " \
              "AND a.artist_name = %s " \
              "AND s.duration = %s"

# Finding the location of artists for those with data on latitude and longitude
artist_location_select = "SELECT s.id song_id, a.id artist_id, s.title, a.artist_name, a.artist_location, a.artist_latitude, a.artist_longitude " \
                         "FROM songs s " \
                         "JOIN artists a " \
                         "ON s.artist_id = a.id " \
                         "WHERE a.artist_latitude IS NOT NULL AND " \
                         "a.artist_longitude IS NOT NULL;"

# QUERY LISTS

# A list of create and drop table queries to make calling multiple queries quick
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
