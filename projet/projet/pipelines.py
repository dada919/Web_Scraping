# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

class SQLitePipeline:
    def open_spider(self, spider):
        self.conn = sqlite3.connect('scraping.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS scraping (
                            id INTEGER PRIMARY KEY,
                            nom TEXT,
                            description TEXT
                            )''')
        self.conn.commit()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute('''INSERT INTO scraping (nom, description) VALUES (?, ?)''',
                         (item['nom'], item['description']))
        self.conn.commit()
        return item
