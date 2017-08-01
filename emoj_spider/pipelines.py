# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import text

class EmojSpiderPipeline(object):
    emoj_sql_template = """
    INSERT INTO emoj (title, image_url, image_backup_url, created_at, updated_at)
    VALUES (:title, :image_url, :image_backup_url, now(), now())
    on conflict (image_url) do update set
    title = EXCLUDED.title,
    image_url = EXCLUDED.image_url,
    image_backup_url = EXCLUDED.image_backup_url,
    updated_at = EXCLUDED.updated_at
    """
    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        engine = create_engine(URL(**self.settings.get('DATABASE')))
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        execute_sql_template = self.emoj_sql_template
        self.session.execute(text(execute_sql_template), item)

        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
        return item
