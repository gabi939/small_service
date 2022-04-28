import json
import os
from flask import Flask,request
import requests

app = Flask(__name__)


@app.route("/api/resource", methods=['GET', 'POST'])
def service():

    if request.method == 'POST':
        data = request.data
        print("I got message")

        try:
            os.remove("/tmp/temp.json")
        except Exception:
            pass

        with open("/tmp/temp.json", "w+") as file:
            json.dump(data,file)

        requests.post(url="34.121.14.255/api/update",data=data)
        return 200
    else:
        print("lets return a message")

        try:
            with open("/tmp/temp.json", "r") as file:
                data = json.load(file)
            return data

        except Exception:
            return 500



@app.route("/api/update")
def service_update():
    print("Got updated")
    data = request.data

    try:
        os.remove("/tmp/temp.json")
    except Exception:
        pass

    with open("/tmp/temp.json", "w+") as file:
        json.dump(data, file)


app.run()