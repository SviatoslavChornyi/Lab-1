__version__ = '0.1.0'

from flask import Flask
from waitress import serve


app = Flask(__name__)




@app.route("/api/v1/hello-world-14")
def hello1():
    return"Hello world(31)"




if __name__ == "__main__" :
   #app.run('0.0.0.0',port=server_port)
   serve(app)