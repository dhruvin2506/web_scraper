from abc import ABC, abstractmethod
from typing import List, Dict, Optional, Any
import logging
import requests
from bs4 import BeautifulSoup

class BaseScraper(ABC):
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            filename='logs/scraper.log',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def get_page(self, url: str, params: Optional[Dict[str, Any]] = None) -> BeautifulSoup:
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            self.logger.error(f"Error fetching {url}: {str(e)}")
            raise
    
    @abstractmethod
    def scrape(self) -> List[Dict]:
        """Abstract method that must be implemented by child classes"""
    pass