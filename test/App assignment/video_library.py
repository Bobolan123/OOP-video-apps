"""
    This module will be used to manage all videos
    by connecting to PostgreSqL and giving out some methods
    Author: Lan IT
"""
from pg_utils import PostgresDB as pgdb

def list_all(): 
    """ 
    Function returns all videos in the DB
    input: None
    output: list of video names
    """
    db = pgdb()
    all_videos = db.select_all_videos()
    video_names = []
    for row in all_videos:
        video_item = f"{row[0]} {row[1]} - {row[2]} {'*' * int(row[3])}"        
        video_names.append(video_item)
    return video_names

class Video:
    def __init__(self, id):
        """
        Explain some attributes of class here
        name_attribute: data type
        """
        self.id = id
        self.name = None 
        self.director = None
        self.rate = 0
        self.play_count = 0
        self.file_path = None
        self.get_video_info_by_id()
        return
    
    def get_video_info_by_id(self):
        #Query DB to get all attributes
        db = pgdb()
        row = db.select_video(self.id)
        self.name = row[1]
        self.director = row[2]
        self.rate = row[3]
        self.play_count = row[4]
        self.file_path = row[5]
        return f"{self.name}\n{self.director}\nrating: {str(self.rate)}\nplays: {str(self.play_count)}\n"
    
    def get_name(self):
        return self.name
    
    def get_director(self):
        return self.director
    
    def get_rating(self):
        return self.rate
    
    def set_rating(self, rate_val):
        self.rate = rate_val
        self.update_video_to_db()
        return
    
    def get_play_count(self):
        return self.play_count
    
    def increament_play_count(self, increase_num=1):
        self.play_count += increase_num
        self.update_video_to_db()
        return
    
    def update_video_to_db(self):
        db = pgdb()
        row_tuple = (self.id, 
                     self.name, 
                     self.director, 
                     self.rate, 
                     self.play_count, 
                     self.file_path)
        db.update_row(row_tuple)
        return
    

