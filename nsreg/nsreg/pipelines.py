# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import psycopg2
from itemadapter import ItemAdapter


class NsregPipeline:
    def __init__(self):
        hostname = 'localhost'
        username = 'nsreg'
        password = 'Nsreg123' # your password
        database = 'nsreg'
        port = '50432'
        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database, port=port)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        """    name = scrapy.Field()
    note1 = scrapy.Field()
    note2 = scrapy.Field()
    city = scrapy.Field()
    website = scrapy.Field() """
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS regcomp(
            id serial PRIMARY KEY, 
            name VARCHAR(255),
            note1 text,
            note2 text,
            city VARCHAR(255),
            website text
        )
        """)

    def process_item(self, item, spider):
        return item
