'''Data Representation - Winter 2022
Big Project: rest_server.py
Author: Ross Downey (G00398275)
Lecturer: Andrew Beatty'''

from flask import Flask,url_for, request, abort, jsonify # import necessary functions from flask

from nflDAO import nflDAO

app = Flask(__name__, static_url_path='', static_folder='static_pages')

# array of quarterbacks
quarterbacks=[
    {"id": 1, "Name": "Patrick Mahomes", "Team": "Kansas City Chiefs", "Passing Yards": 3585, "TDs": 29, "INTs": 8},
    {"id": 2, "Name": "Josh Allen", "Team": "Buffalo Bills", "Passing Yards": 3183, "TDs": 23, "INTs": 11},
    {"id": 3, "Name": "Joe Burrow", "Team": "Cincinnati Bengals", "Passing Yards": 3160, "TDs": 23, "INTs": 8}
]
# global variable needed for create function
nextId = 4

# Test getAll function using: curl http://127.0.0.1:5000/quarterbacks
@app.route('/quarterbacks')
def getAll():
    return jsonify(quarterbacks)

# Test findById function using: curl http://127.0.0.1:5000/quarterbacks/1 for example
@app.route('/quarterbacks/<int:id>')
def findById(id):
    foundQBs = list(filter(lambda t : t["id"] == id, quarterbacks)) # lambda function
    if len(foundQBs) == 0:
        return jsonify({}), 204 # 204 code, no content
    return jsonify(foundQBs[0])


# Test create function using curl -X POST -H "content-type:application/json" -d "{\"Name\": \"Tom Brady\",\"Team\": \"Tampa Bay Buccaneers\", \"Passing Yards\": 3000, \"TDs\": 14, \"INTs\": 2}" http://127.0.0.1:5000/quarterbacks
@app.route('/quarterbacks', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400) # 400 code, bad request if not in json format
    QB = {
        "id": nextId,
        "Name": request.json["Name"],
        "Team": request.json["Team"],
        "Passing Yards": request.json["Passing Yards"], 
        "TDs": request.json["TDs"],
        "INTs": request.json["INTs"]
    }
    quarterbacks.append(QB)
    nextId += 1 
    return jsonify(QB)


# Test update function using: curl -X PUT -d "{\"Passing Yards\": 4000, \"TDs\": 30,\"INTs\": 20}" -H "content-type:application/json" http://127.0.0.1:5000/quarterbacks/1
@app.route('/quarterbacks/<int:id>', methods=['PUT'])
def update(id):
    foundQBs = list(filter(lambda t: t["id"] == id,quarterbacks))
    if len(foundQBs) == 0:
        return jsonify({}), 404 # If book not found to update return bad request error code
    currentQB = foundQBs[0]
    if 'Name' in request.json:
        currentQB['Name'] = request.json['Name']
    if 'Team' in request.json:
        currentQB['Team'] = request.json['Team']
    if 'Passing Yards' in request.json:
        currentQB['Passing Yards'] = request.json['Passing Yards'] 
    if 'TDs' in request.json:
        currentQB['TDs'] = request.json['TDs']
    if 'INTs' in request.json:
        currentQB['INTs'] = request.json['INTs']
    return jsonify(currentQB)

# Test delete function using: curl -X DELETE http://127.0.0.1:5000/quarterbacks/1
@app.route('/quarterbacks/<int:id>', methods=['DELETE'])
def delete(id):
    foundQBs = list(filter(lambda t: t["id"] == id, quarterbacks))
    if len(foundQBs) == 0:
        return jsonify({}), 404 
    quarterbacks.remove(foundQBs[0])

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug = True) 