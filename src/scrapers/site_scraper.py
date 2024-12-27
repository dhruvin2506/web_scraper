from typing import List, Dict
from .base_scraper import BaseScraper
from ..database.db_handler import DatabaseHandler

class SiteScraper(BaseScraper):
    def __init__(self, base_url: str, db_handler: DatabaseHandler):
        super().__init__(base_url)
        self.db_handler = db_handler
        
    def scrape(self) -> List[Dict]:
        try:
            soup = self.get_page(self.base_url)
            data = []
            
            books = soup.find_all('article', class_='product_pod')
            for book in books:
                item_data = {
                    'title': book.h3.a['title'],
                    'price': book.find('p', class_='price_color').text,
                    'description': book.h3.a['title'],
                    'url': book.find('h3').find('a')['href']
                }
                data.append(item_data)
                
            self.db_handler.insert_many(data)
            self.logger.info(f"Scraped {len(data)} books")
            return data
            
        except Exception as e:
            self.logger.error(f"Scraping error: {str(e)}")
            raise