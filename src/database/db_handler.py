import sqlite3
from typing import List, Dict
import logging

class DatabaseHandler:
    def __init__(self, db_path: str = 'data/scraper.db'):
        self.db_path = db_path
        self.setup_logging()
        self.setup_database()
    
    def setup_logging(self):
        self.logger = logging.getLogger(__name__)
    
    def setup_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS scraped_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    price TEXT,
                    description TEXT,
                    url TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
    
    def insert_many(self, items: List[Dict]):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.executemany(
                '''INSERT INTO scraped_data (title, price, description, url)
                   VALUES (:title, :price, :description, :url)''',
                items
            )