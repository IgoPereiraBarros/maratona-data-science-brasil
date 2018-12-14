import MySQLdb as sql

class Database:

	def __init__(self):
		self.connection = sql.connect(user='root', passwd='', port=3306, host='127.0.0.1', db='datamining')
		self.cursor = self.connection.cursor()

	def insert(self, query):
		try:
			self.cursor.execute(query)
			self.connection.commit()
		except:
			self.connection.rollback()

	def selectAll(self):
		data = []
		users = []
		items = []
		ratings = []
		
		self.cursor.execute("SELECT rating, Users_idUsers, Recipe_idRecipe FROM rating")
		rows = self.cursor.fetchall()

		for r in rows:
			ratings.append(r[0])
			users.append(r[1])
			items.append(r[2])

		data.append(users)
		data.append(items)
		data.append(ratings)

		return data


