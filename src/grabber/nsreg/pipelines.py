# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import psycopg2

SQL_CREATE_REGCOMP_TABLE = '''
CREATE TABLE IF NOT EXISTS regcomp(
            id serial PRIMARY KEY,
            name VARCHAR(255) UNIQUE,
            note1 text,
            note2 text,
            city VARCHAR(255),
            website text,
            price_reg decimal,
            price_prolong decimal,
            price_change decimal
        )
'''

SQL_UPDATE_REGCOMP = '''
INSERT INTO regcomp (name, note1, note2, city, website, price_reg, price_prolong, price_change)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT (name) DO UPDATE
SET ( note1, note2, city, website, price_reg, price_prolong, price_change) = (
    COALESCE(%s, regcomp.note1),
    COALESCE(%s, regcomp.note2),
    COALESCE(%s, regcomp.city),
    COALESCE(%s, regcomp.website),
    COALESCE(%s, regcomp.price_reg),
    COALESCE(%s, regcomp.price_prolong),
    COALESCE(%s, regcomp.price_change)
    )
RETURNING id
'''


class NsregPipeline:
    def __init__(self):
        hostname = os.environ['HOSTNAME_DB']
        username = os.environ['USERNAME_DB']
        password = os.environ['PASSWORD_DB']  # your password
        database = os.environ['DATABASE_NAME']
        port = os.environ['PORT_DB']
        # Create/Connect to database
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database, port=port)

        # Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        # Create quotes table if none exists
        self.cur.execute(SQL_CREATE_REGCOMP_TABLE)
        self.connection.commit()

    def process_item(self, item, spider):
        price = item.get('price', {
            'price_reg': None,
            'price_prolong': None,
            'price_change': None,
        })
        self.cur.execute(SQL_UPDATE_REGCOMP, (
            item['name'],
            item.get('note1', None),
            item.get('note2', None),
            item.get('city', None),
            item.get('website', None),
            price.get('price_reg', None),
            price.get('price_prolong', None),
            price.get('price_change', None),
            item.get('note1', None),
            item.get('note2', None),
            item.get('city', None),
            item.get('website', None),
            price.get('price_reg', None),
            price.get('price_prolong', None),
            price.get('price_change', None),
        ))
        spider.logger.info('Saving item SQL: %s', self.cur.query)

        # self.cur.execute("SELECT * FROM regcomp WHERE name = %s", (item['name'],))
        # result = self.cur.fetchone()

        # Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()
