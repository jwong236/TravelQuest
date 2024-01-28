from tourist import TouristClass
from utils.quest import Quest
from quester import Quester
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET', 'POST'])
def main1():
    print("Hello")
    print(request.json)
    t = TouristClass()
    t.fetch_current_location()
    print(t.longitude)
    print(t.latitude)
    # print(t.get_nearby_poi())
    print(jsonify(t.get_nearby_poi()))
    return jsonify(t.get_nearby_poi())

def main2():
    q = Quester()
    print(q.generate_quests("daily"))
    

if __name__ == "__main__":
    main2()