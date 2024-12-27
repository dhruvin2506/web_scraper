import yaml
from src.scrapers.site_scraper import SiteScraper
from src.database.db_handler import DatabaseHandler

def load_config():
    with open('config/config.yaml', 'r') as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    db_handler = DatabaseHandler(config['database']['path'])
    scraper = SiteScraper(config['scraping']['base_url'], db_handler)
    
    try:
        data = scraper.scrape()
        print(f"Successfully scraped {len(data)} items")
    except Exception as e:
        print(f"Error during scraping: {str(e)}")

if __name__ == "__main__":
    main()