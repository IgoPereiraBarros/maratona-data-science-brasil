import requests
import re

from DataBaseCon import Database

url = 'http://127.0.0.1/dashboard/recipes/Recipe'
conn = Database()

def getSourceCode(id):
	r = requests.get(url + str(id) + '.html')
	return r.text

def getUsers():
	users = []
	for i in range(1, 10):
		sourceCode = getSourceCode(i)
		for match in re.findall('<p id="userId">([0-9]+)', sourceCode):
			if match not in users:
				users.append(match)
				#Database.insert(conn, "INSERT INTO users (userName) VALUES ("+match+");")
	return users

def getRecipe():
	recipes = []
	for i in range(1, 10):
		sourceCode = getSourceCode(i)
		for match in re.findall('<title>(.*)</title>', sourceCode):
			if match not in recipes:
				recipes.append(match)
				#Database.insert(conn, "INSERT INTO recipe (recipeName) VALUES ('"+match+"');")
	return recipes

def getRatings():
	ratings = []

	for i in range(1, 10):
		foundRetings = []
		j = 0
		sourceCode = getSourceCode(i)

		for match in re.findall('<p id="rating">([0-9]+)', sourceCode):
			foundRetings.append(match)

		for match in re.findall('<p id="userId">([0-9]+)', sourceCode):
			ratings.append([foundRetings[j], match, i])
			#Database.insert(conn, "INSERT INTO rating (rating, Users_idUsers, Recipe_idRecipe) VALUES ("+str(foundRetings[j])+", (SELECT idUsers FROM users WHERE userName = "+match+"), "+str(i)+" );")
			j += 1
	return ratings


print(getUsers())
print(getRecipe())
print(getRatings())