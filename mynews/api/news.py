import os
from pymongo import MongoClient
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)
print('app path: %s' % app)
mongo = PyMongo(app)

db_name = 'my_news'
table_name = 'news_content'


def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db


MONGODB_URI = os.environ.get('MONGODB_URI')
if not MONGODB_URI:
    mongoClient = MongoClient('localhost', 27017)
    db = mongoClient[db_name]
else:
    db = MongoClient(MONGODB_URI)[db_name]


def to_json(data):
    return json.dumps(data, default=json_util.default)


# @classmethod
# def from_crawler(cls, crawler):
#     return cls(
#         mongo_uri=crawler.settings.get('MONGO_URI'),
#         mongo_db=crawler.settings.get('MONGO_DATABASE', 'news_items')
#     )

@app.route('/news/title', methods=['GET'])
def get_news_title():
    if request.method == 'GET':
        results = db[table_name].find({}, {'title': 1})
        json_results = []
        for result in results:
            json_results.append(result)
        return to_json(json_results)


@app.route('/news', methods=['GET'])
def get_news():
    if request.method == 'GET':
        results = db[table_name].find()
        json_results = []
        print('======result=====%s' % db)
        for result in results:
            json_results.append(result)
        return to_json(json_results)


@app.route('/title/single_news', methods=['GET'])
def get_single_news_title():
    if request.method == 'GET':
        title = request.args.get('title')
        result = db[table_name].find({'title': title})
        return str(json_util.dumps(result))


@app.route('/single_news', methods=['GET'])
def get_single_news():
    if request.method == 'GET':
        object_id = ObjectId(request.args.get('id'))
        result = db[table_name].find({'_id': object_id})
        # cover_result = json_util.dumps(result)
        # import pdb; pdb.set_trace()
        return json_util.dumps(result)


if __name__ == '__main__':
    app.run()
