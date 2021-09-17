import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect("youtube_data.db")



def CreateExcelFile(con, q, filename):
    df = pd.read_sql_query(q, con)
    
    df.to_excel('Excel_files/'+filename+'.xlsx', index=False, header=True)
    # con.close()


# Quries
# Tags vs Number Videos
q1 = "SELECT tags.name AS Tags, count(videos.id) AS video_name FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) GROUP BY tags.id;"
filename1 = 'tagsvsvideos'
# Tags vs Most and Least Videos
q2 = "SELECT tags.name AS Tags, max(videos.id) as Most_Videos , min(videos.id) AS Least_Videos FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id)"
filename2 = 'tageWithMostAndLeastVideos'
# Tags vs Average Duration of videos
q3 = "SELECT tags.name AS Tags, avg(videos.duration) AS AVG_Duration FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) GROUP BY tags.id;"
filename3 = 'AvgDurationOfVideos'
# Tag with most video time, least video time
q4 = "SELECT tags.name AS Tags, max(videos.duration) AS Most_Video_Time, min(videos.duration) AS Least_Video_Time FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) GROUP BY tags.id;"
filename4 = 'mostAndLeastVideoTime'

#Classify tags as Tutorials, demos, live coding
# Tags as Tutorials
q5 = "SELECT tags.name AS Tutorials FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) where tags.name like '%tutorial%' GROUP BY tags.id;"
filename5 = 'tags_as_tutorials'
# Tags as demos
q6 = "SELECT tags.name AS demos FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) where tags.name like '%demos%' GROUP BY tags.id;"
filename6 = 'tags_as_demos'
# Tags as coding
q7 = "SELECT tags.name AS Live_Coding FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) where tags.name like '%cod%' GROUP BY tags.id;"
filename7 = 'tags_as_liveCoding'


# # Drivers
CreateExcelFile(con, q1, filename1)
CreateExcelFile(con, q2, filename2)
CreateExcelFile(con, q3, filename3)
CreateExcelFile(con, q4, filename4)
CreateExcelFile(con, q5, filename5)
CreateExcelFile(con, q6, filename6)
CreateExcelFile(con, q7, filename7)


# Bounce
bonus = "SELECT tags.name AS Tags, sum(videos.comment_count) AS Comments, sum(videos.view_count) AS View, sum(videos.like_count) AS Like FROM ((videos_vs_tags INNER JOIN videos on videos_vs_tags.tag_id = tags.id) INNER JOIN tags on videos_vs_tags.video_id = videos.id) Group BY tags.id"
bonus_file = 'Bonus'

CreateExcelFile(con, bonus, bonus_file)

con.close()