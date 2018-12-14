from flask import Flask, jsonify, request

app = Flask(__name__)

languagens = [{'name':'Python'}, {'name':'Java'}, {'name':'CSharp'}, {'name':'Ruby'}]

@app.route('/', methods=['GET'])
def init():
	return jsonify({'message' : 'When I was child'})

@app.route('/lang', methods=['GET'])
def returnAll():
	return jsonify({'Languagens' : languagens})

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
	langs = [language for language in languagens if language['name']==name]
	return jsonify({'Language' : langs[0]})

@app.route('/lang', methods=['POST'])
def addOne():
	language = {'name' : request.json['name']}

	languagens.append(language)
	return jsonify({'language' : languagens})

@app.route('/lang/<string:name>', methods=['PUT'])
def editOne(name):
	langs = [language for language in languagens if language['name'] == name]

	langs[0]['name'] = request.json['name']
	return jsonify({'language' : langs[0]})

@app.route('/lang/<string:name>', methods=['DELETE'])
def removeOne(name):
	langs = [language for language in languagens if language['name'] == name]
	languagens.remove(langs[0])
	return jsonify({'languagens' : languagens})

if __name__ == '__main__':
	app.run(debug=True, port=8080)