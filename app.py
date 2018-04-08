import os
from flask import Flask, request


app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def getAuthToken():
  data = request.get_json() # a multidict containing POST data
  print(data)
  return data



if __name__ == '__main__':

    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)