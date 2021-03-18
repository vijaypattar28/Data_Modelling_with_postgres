# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplays 
        (
          songplay_id SERIAL PRIMARY KEY
        , start_time time not null
        , user_id int not null
        , level varchar not null
        , song_id varchar
        , artist_id varchar
        , session_id varchar not null
        , location varchar not null
        , user_agent varchar not null
        , foreign key(start_time) references time(start_time)
        , foreign key(user_id) references users(user_id)
        , foreign key(song_id)references songs(song_id)
        , foreign key(artist_id) references artists(artist_id)
        );
""")

user_table_create = ("""
create table if not exists users
        (
          user_id int primary key
        , first_name varchar not null
        , last_name varchar not null
        , gender varchar not null
        , level varchar not null
        )  ;
""")

song_table_create = ("""
create table if not exists songs
        (
          song_id varchar primary key
        , title varchar not null
        , artist_id varchar not null
        , year int not null
        , duration real not null
        ) ;
""")

artist_table_create = ("""
create table if not exists artists
        (
          artist_id varchar primary key
        , name varchar not null
        , location varchar not null
        , latitude float not null
        , longitude float not null
        );
""")

time_table_create = ("""
create table if not exists time
        (
          start_time  time primary key
          , hour int not null
          , day int not null
          , week int not null
          , month int not null
          , year int not null
          , weekday int not null
          );
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays 
        (
            start_time
          , user_id
          , level
          , song_id
          , artist_id
          , session_id
          , location
          , user_agent
        )
        values
        (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""insert into users
        (
          user_id
        , first_name
        , last_name
        , gender
        , level
        )
        values
        (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING;;
""")

#song_table_insert = ("""insert into song_table
#        (
#          song_id
#        , title
#        , artist_id
#        , year
#        , duration
#        )
#        values
#        (%s, %s, %s, %s, %s) 
#        ON CONFLICT DO NOTHING;
#""")

song_table_insert = ("""
INSERT INTO songs (
    song_id,
    title,
    artist_id,
    year,
    duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

artist_table_insert = ("""insert into artists
        (
          artist_id
        , name
        , location
        , latitude
        , longitude
        )
        values
        (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
""")


time_table_insert = ("""insert into time(
          start_time
          , hour
          , day
          , week
          , month
          , year
          , weekday
          )
        values
        (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id , a.artist_id
    FROM artists a
    JOIN songs s
    ON s.artist_id = a.artist_id
    WHERE s.title = (%s) AND a.name = (%s) AND s.duration = (%s);

""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]