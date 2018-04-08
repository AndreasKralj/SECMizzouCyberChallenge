import os
from flask import Flask, request


app = Flask(__name__)

@app.route('/login', methods = ['POST'])
def getAuthToken():
  data = request.form # a multidict containing POST data
  print(data)



if __name__ == '__main__':

    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)