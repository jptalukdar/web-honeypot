from flask import Flask
from flask import request
import datetime
import json
import base64
app = Flask(__name__)


def writeToLogFile(data:dict):
    with open("honey.jsonlog","a") as fp:
        fp.write(json.dumps(data))
        fp.write("\n")

@app.route("/", methods=['POST','GET','PUT','DELETE','HEAD'])
@app.route("/<path:path>" , methods=['POST','GET','PUT','DELETE','HEAD'])
def hello_world(path="/"):
    data = {}
    data['url'] = str(request.url)
    data['time'] = str(datetime.datetime.now())
    data['request_method'] = str(request.method)
    data['source'] = str(request.remote_addr)
    data['headers'] = { str(k):str(v) for k,v in request.headers.items() }
    data['body'] = str(base64.b64encode(request.get_data()))
    print(data)
    writeToLogFile(data)
    return f"<p>Hello, World!</p>: {path} {request.url}"