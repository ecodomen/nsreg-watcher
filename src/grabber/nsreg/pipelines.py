import os
import psycopg2

SQL_CREATE_TABLES = """
CREATE TABLE domain (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY (id),
);

CREATE TABLE parse_history (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY (id),
);

CREATE TABLE price (
    id BIGINT GENERATED ALWAYS AS IDENTITY,
    id_parse INT,
    price_reg DECIMAL,
    price_prolong DECIMAL,
    price_change DECIMAL,
    PRIMARY KEY (id),
    CONSTRAINT id_registrator
        FOREIGN KEY (id)
        REFERENCES registrator (id)
        ON DELETE CASCADE,
    CONSTRAINT id_domain
        FOREIGN KEY (id)
        REFERENCES domain (id)
        ON DELETE SET NULL,
    CONSTRAINT id_parse
        FOREIGN KEY (id)
        REFERENCES parse_history (id)
        ON DELETE CASCADE,
);
"""


SQL_UPDATE_PRICE = """
DO
$do$

    DECLARE price_reg DECIMAL;
    DECLARE price_prolong DECIMAL;
    DECLARE price_change DECIMAL;

BEGIN

    SELECT DISTINCT ON (id_registrator) price_reg, price_prolong, price_change
    INTO price_reg, price_prolong, price_change
    FROM price
    WHERE id_registrator = %(registrator)s
    ORDER BY id_registrator, id_parse DESC;

    IF NOT FOUND OR
    price_reg != %(price_reg)s OR price_prolong != %(price_prolong)s OR price_change != %(price_change)s
    THEN
        INSERT INTO price (id_registrator, id_domain, id_parse,
        price_reg, price_prolong, price_change)
        VALUES (%(registrator)s, %(domain)s, %(parse)s,
        %(price_reg)s, %(price_prolong)s, %(price_change)s);
    END IF;

END
$do$
"""


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
        self.cur.execute(SQL_CREATE_TABLES)
        self.connection.commit()

    def process_item(self, item, spider):

        def get_parse_num() -> int:
            ...

        def get_registrator_id(name: str) -> int:
            ...

        price = item.get('price', {
            'price_reg': None,
            'price_prolong': None,
            'price_change': None,
        })

        name = item.get('name')
        registrator_id = get_registrator_id(name)

        parse = get_parse_num()

        self.cur.execute(SQL_UPDATE_PRICE, {
            'registrator': registrator_id,
            'domain': 1,  # 'RU'
            'parse': parse,
            'price_reg': price['price_reg'],
            'price_prolong': price['price_prolong'],
            'price_change': price['price_change'],
        })

        spider.logger.info('Saving item SQL: %s', self.cur.query)

        # self.cur.execute("SELECT * FROM registrator WHERE name = %s", (item['name'],))
        # result = self.cur.fetchone()

        # Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()
