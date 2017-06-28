import pymongo
from bson import json_util
from flask import Flask, request
from flask_pymongo import PyMongo
import json

app = Flask(__name__)
mongo = PyMongo(app)

collection_name = 'scrapy_items'


def __init__(self, mongo_uri, mongo_db):
    self.mongo_uri = mongo_uri
    self.mongo_db = mongo_db


mongoClient = pymongo.MongoClient('localhost', 27017)
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
        results = db['news_content'].find({}, {"title" : 1})
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


if __name__ == '__main__':
    app.run()
