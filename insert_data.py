

def insert_data_to_db(cursor, conn, filtered_data):
    tag_counter = 0
    for counter, obj in enumerate(filtered_data, start=1):
        duration = obj['content_details']['duration']
        # print(duration)
        hour_check = True
        minute_check = True
        if duration.find('H') != -1:
            hours = duration[duration.find('T') + 1:duration.find('H')]
        else:
            hours = 0
            hour_check = False

        if duration.find('M') != -1:
            minutes = (
                duration[duration.find('H') + 1 : duration.find('M')]
                if hour_check
                else duration[duration.find('T') + 1 : duration.find('M')]
            )

        else:
            minutes = 0
            minute_check = False


        if duration.find('S') == -1:
            seconds = 0
        elif not minute_check:
            minutes = duration[duration.find('H') + 1:duration.find('S')]
        else:
            seconds = duration[duration.find('M') + 1:duration.find('S')]
        total_duration_seconds = int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)
        try:
            view_count = obj['statistics']['viewCount']
        except Exception as e:
            # print(e)
            view_count = 0

        try:
            like_count = obj['statistics']['likeCount']
        except Exception as e:
            # print(e)
            like_count = 0

        try:
            dislike_count = obj['statistics']['dislikeCount']
        except Exception as e:
            # print(e)
            dislike_count = 0

        try:
            favorite_count = obj['statistics']['favoriteCount']
        except Exception as e:
            # print(e)
            favorite_count = 0

        try:
            comment_count = obj['statistics']['commentCount']
        except Exception as e:
            # print(e)
            comment_count = 0


        cursor.execute("Insert into videos values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (counter, obj['video_id'], obj['snippet']['title'], obj['snippet']['channel_title'], obj['snippet']['publish_time'],
                       total_duration_seconds, view_count, like_count, dislike_count, favorite_count, comment_count))

        try:
            for tag in obj['snippet']['tags']:
                sql_query = f'SELECT * FROM tags WHERE name="{tag}" COLLATE NOCASE;'
                cursor.execute(sql_query)
                res = cursor.fetchall()

                tag_counter += 1
                if res:
                    # print(res[0][0])
                    sql_query_1 = 'INSERT into videos_vs_tags values(?, ?, ?)'
                    cursor.execute(sql_query_1, (tag_counter, counter, res[0][0]))
                else:

                    sql_query = 'INSERT into tags values(?, ?)'
                    cursor.execute(sql_query, (tag_counter, tag))

                    sql_query_1 = 'INSERT into videos_vs_tags values(?, ?, ?)'
                    cursor.execute(sql_query_1, (tag_counter, counter, tag_counter))

        except Exception as e:
            pass

        conn.commit()
    conn.close()
