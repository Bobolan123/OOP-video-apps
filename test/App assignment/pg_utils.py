"""
This module contains some utilities for DB connecting and quering 
"""
import sys
import psycopg2 as pg	
import configDB

class PostgresDB:
	def __init__(self, conn_string=configDB.DB_CONN):
		self.conn_string = conn_string
		self.conn = None
		self.cursor = None
		return
	
	def connectDB(self):
		try:
			#Connect to Db
			self.conn = pg.connect(self.conn_string)
			#Define the cursor
			self.cursor = self.conn.cursor()
		except Exception as e:
			print(f"Got erros on DB connection: {e}")
			sys.exit()
	
	def close(self):
		self.cursor.close()
		self.conn.close()

	def select_all_videos(self):
		self.connectDB()
		# Define a connection to postgresql server
		query_string = "SELECT * FROM videos ORDER BY id DESC"
		self.cursor.execute(query_string)
		results = self.cursor.fetchall()
		self.close()
		return results
	
	def select_video(self, video_id):
		self.connectDB()
		query_string = f"SELECT * FROM videos WHERE id = {video_id}"
		self.cursor.execute(query_string)
		results = self.cursor.fetchall()
		self.close()
		return results[0]
	
	def select_video_by_name(self, director):
		self.connectDB()
		query_string = f"SELECT * FROM videos WHERE director = '{director}'"
		self.cursor.execute(query_string)
		results = self.cursor.fetchall()
		self.close()
		return results

	def update_row(self, row_tuples):
		self.connectDB()
		query_string = f"UPDATE table_name\
						SET video_name = {row_tuples[1]},\
							director = {row_tuples[2]},\
							rate = {row_tuples[3]}, \
							play_count={row_tuples[4]},\
							file_path = {row_tuples[5]}\
						WHERE id = {row_tuples[0]}"
		self.cursor.execute(query_string)
		self.conn.commit()
		self.cursor.close()
		return
	
