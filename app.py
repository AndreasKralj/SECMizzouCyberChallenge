import os
from flask import Flask, request


app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def getAuthToken():
  data = request.get_json() # a multidict containing POST data
  print(data)
  print(data['username'])
  return 'true\n'



if __name__ == '__main__':

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)