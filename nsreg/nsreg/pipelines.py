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
            website text, 
            pricereg text, 
            pricecont text, 
            pricetrans text
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("SELECT * FROM regcomp WHERE name = %s", (item['name'],))
        result = self.cur.fetchone()

        if result:
            spider.logger.warn("Item already in database: %s" % item['name'])
        else:
            pricereg, pricecont, pricetrans = '', '', ''
            if item['price']:
                pricereg, pricecont, pricetrans = item['price']['pricereg'], item['price']['pricecont'], item['price']['pricetrans'] 

            self.cur.execute(""" INSERT INTO regcomp (name, note1, note2, city, website, pricereg, pricecont, pricetrans) values (%s,%s,%s,%s,%s,%s,%s,%s)""", (
                item["name"], 
                item["note1"], 
                item["note2"],
                item["city"],
                item["website"],     
                pricereg, 
                pricecont, 
                pricetrans 
            ))

            ## Execute insert of data into database
            self.connection.commit()
        return item
    
    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()

