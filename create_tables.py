from connection import *


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"youtube_data.db"

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        sql_create_tags_table = """ CREATE TABLE IF NOT EXISTS tags (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL
                                    ); """

        # create tags table
        create_table(conn, sql_create_tags_table)
        print('done 1')
        sql_create_videos_table = """CREATE TABLE IF NOT EXISTS videos (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    video_id text NULL,
                                    title text NOT NULL,
                                    channel_title text NOT NULL,
                                    publish_time text NOT NULL,
                                    duration integer NOT NULL,
                                    view_count integer NOT NULL,
                                    like_count integer NOT NULL,
                                    dislike_count integer NOT NULL,
                                    favorite_count integer NOT NULL,
                                    comment_count integer NOT NULL
                                );"""
        # create videos table
        create_table(conn, sql_create_videos_table)
        print('done 2')
        sql_create_videosvstags_table = """
                                    CREATE TABLE IF NOT EXISTS videos_vs_tags (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        video_id integer NOT NULL,
                                        tag_id integer NOT NULL,
                                        FOREIGN KEY (video_id) REFERENCES videos (id),
                                        FOREIGN KEY (tag_id) REFERENCES tags (id)
                                    );
                                    """


        # create videos vs tags table
        create_table(conn, sql_create_videosvstags_table)
        print('done 3')
        conn.close()

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()