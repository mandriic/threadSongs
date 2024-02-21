import psycopg2
from psycopg2 import sql
def modificate_table(command, data):
    dbname = 'songs'
    user = 'sirius'
    password = ''
    host = 'localhost'  
    port = '5432'
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        create_table_query = sql.SQL("""CREATE TABLE IF NOT EXISTS songstab
                                    (title varchar(50),
                                    artist varchar(50),
                                    album varchar (50),
                                    duration int)""")
        cursor.execute(create_table_query)
        if command == "add":
            insert_query = """
                INSERT INTO songstab (title, artist, album, duration)
                VALUES ('{}', '{}', '{}', '{}')
                """.format(data['title'], data['artist'], data['album'], data['duration'])
            cursor.execute(insert_query, data)
        elif command == "delete":
            delete_query = """
                DELETE FROM songstab
                WHERE title = '{}'
                """.format(data['title'])
            cursor.execute(delete_query, data)
        elif command == "patch":
            patch_query = """
                UPDATE songstab
                SET duration = '{}', album = '{}'
                WHERE title = '{}'
                """.format(data['duration'], data['album'], data['title'])
            cursor.execute(patch_query, data)
        elif command == "get" and data != None:
            get_query = """
                SELECT * FROM songstab
                WHERE title = '{}'
                """.format(data['title'])
            cursor.execute(get_query, data)
            result = cursor.fetchall()
            print(result)
        elif command == "get" and data == None:
            get_query = """
                SELECT * FROM songstab
                """
            cursor.execute(get_query)
            result = cursor.fetchall()
            print(result)
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()