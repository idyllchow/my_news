# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

from mynews.mynews import settings


class MynewsPipeline(object):

    #连接数据库
    def __init__(self):
        connection = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])

        #数据库
        db = connection[settings['MONGODB_DB']]
        # self.table = db[settings['MONGODB_TABLE']]
        self.connection=db[settings['MONGODB_CONNECTION']]


    def process_item(self, item, spider):
        print("###########process_item########")
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem('Missing{0}!'.format(data))
        if valid:
            self.connection.insert(dict(item))
        return item

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item