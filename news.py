import os
import pymongo
from bson import json_util
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import json
from bson.objectid import ObjectId

app = Flask(__name__)
mongo = PyMongo(app)

collection_name = 'scrapy_items'
table_name = 'news_content'


def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db


MONGODB_URI = os.environ.get('MONGODB_URI')
if not MONGODB_URI:
    mongoClient = pymongo.MongoClient('localhost', 27017)
else:
    mongoClient = pymongo.MongoClient(MONGODB_URI)
db = mongoClient['my_news']


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
        results = db['news_content'].find({}, {'title': 1})
        json_results = []
        for result in results:
            json_results.append(result)
        return to_json(json_results)


@app.route('/news', methods=['GET'])
def get_news():
    if request.method == 'GET':
        results = db['news_content'].find()
        json_results = []
        print('======result=====%s' % db)
        for result in results:
            json_results.append(result)
        return to_json(json_results)


@app.route('/title/single_news', methods=['GET'])
def get_single_news_title():
    if request.method == 'GET':
        title = request.args.get('title')
        result = db['news_content'].find({'title': title})
        return str(json_util.dumps(result))


@app.route('/single_news', methods=['GET'])
def get_single_news():
    if request.method == 'GET':
        object_id = ObjectId(request.args.get('id'))
        result = db['news_content'].find({'_id': object_id})
        # cover_result = json_util.dumps(result)
        # import pdb; pdb.set_trace()
        return json_util.dumps(result)


if __name__ == '__main__':
    app.run()
