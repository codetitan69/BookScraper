# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class DemobookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        fields = adapter.field_names()
        for field in fields:
            if field != 'description':
                value = adapter.get(field)
                adapter[field] = value.strip()

        prize_fields = ['prize']
        for field in prize_fields:
            value = adapter.get(field)
            value = value.replace('£','')
            adapter[field] = float(value)

        availability_field = 'availability'
        value = adapter.get(availability_field)
        arr = value.split('(')

        if len(arr) > 1:
            availability_arr = arr[1].split(" ")
            adapter[availability_field] = int(availability_arr[0])
        else:
            adapter[availability_field] = 0

        return item


class DBpipeline:

    def __init__(self):

        self.conn = psycopg2.connect(
            dbname="Scrapy",
            user="postgres",
            password="viper",
            host="localhost",
            port="5432"
        )

        self.cur = self.conn.cursor()

        self.cur.execute("""
                CREATE TABLE IF NOT EXISTS books(
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    category VARCHAR(75) NOT NULL,
                    description TEXT,
                    prize DECIMAL NOT NULL ,
                    availability INTEGER NOT NULL
                );
        """)

    def process_item(self, item, spider):

        self.cur.execute("""
            INSERT INTO books (
                title,
                category,
                description,
                prize,
                availability
            ) values (
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """,(
            item['title'],
            item['category'],
            item['description'],
            item['prize'],
            item['availability']
            )
        )

        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.conn.close()