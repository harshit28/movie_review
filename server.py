import uuid
import os
from flask import Flask, jsonify, request ,current_app, send_from_directory
from flask_cors import CORS
# from .client import client_bp

movieList =[]

app = Flask(__name__,static_folder='./dist/static')




app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})



APP_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(APP_DIR)
DIST_DIR = os.path.join(ROOT_DIR, 'dist')
print(APP_DIR,ROOT_DIR,DIST_DIR)
@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./dist', path)


@app.route('/')
def root():
  return send_from_directory('./dist', 'index.html')


@app.route('/working',methods=['GET'])
def hello_world():
    return 'Hello, World!'
@app.route('/deletereview/<movie_id>', methods=['DELETE'])
def removereview(movie_id):
    response_object = {'status': 'success'}
    for x in movieList:
        if x['id'] == movie_id:
            movieList.remove(x)
    response_object['message'] = 'Book removed!'
    return jsonify(response_object)

@app.route('/getreview',methods=['GET'])
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