# -*- coding: utf-8 -*-
from pprint import pprint
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline:
    def process_item(self, item, spider):
        pprint(item)
        return item
