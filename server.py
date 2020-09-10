import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS

movieList =[]

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/api/working',methods=['GET'])
def hello_world():
    return 'Hello, World!'
@app.route('/api/deletereview/<movie_id>', methods=['DELETE'])
def removereview(movie_id):
    response_object = {'status': 'success'}
    for x in movieList:
        if x['id'] == movie_id:
            movieList.remove(x)
    response_object['message'] = 'Book removed!'
    return jsonify(response_object)

@app.route('/api/getreview',methods=['GET'])
def getMovies():
    
    return jsonify(movieList)

@app.route('/addreview',methods=['POST'])
def addreview():
    movieReview = request.get_json()
    movieReview['id'] = str(uuid.uuid1())
    movieList.append(movieReview)
    return 'Success'

@app.route('/updatereview/<movie_id>',methods=['PUT'])
def updatereview(movie_id):
    movieReview = request.get_json()
    print("req data",movieReview)
    for x in movieList:
        if x['id'] == movie_id:
            x['review'] = movieReview["review"]
            x['rating'] = movieReview["rating"]
    return 'Update Successful'
if __name__ == '__main__':
    app.run(port=5000)